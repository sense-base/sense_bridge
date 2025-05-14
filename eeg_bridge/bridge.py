import numpy as np
from builtin_interfaces.msg import Time as MsgTime
from eeg_msgs.msg import EEGBlock
from std_msgs.msg import Header
import rclpy
from rclpy.time import Time


class EEGBridge:
    @staticmethod
    def numpy_to_eegblock(data: np.ndarray, sampling_rate: float = 256.0, header: Header = None) -> EEGBlock:
        """
        Convert a 2D numpy array of shape (channels, samples) to an EEGBlock message.
        """
        if data.ndim != 2:
            raise ValueError("Input data must be 2D with shape (channels, samples)")

        num_channels, num_samples = data.shape
        eeg_msg = EEGBlock()

        # Metadata
        eeg_msg.num_channels = num_channels
        eeg_msg.num_samples = num_samples
        eeg_msg.sampling_rate = sampling_rate

        # Use provided header or create a default one
        if header is not None:
            eeg_msg.header = header
        else:
            eeg_msg.header = Header(stamp=Time().to_msg())

        # Flatten the data
        eeg_msg.data = data.astype(np.float32).flatten().tolist()

        return eeg_msg

    @staticmethod
    def eegblock_to_numpy(msg: EEGBlock) -> np.ndarray:
        """
        Convert an EEGBlock message back into a 2D numpy array of shape (channels, samples)
        """
        if len(msg.data) != msg.num_channels * msg.num_samples:
            raise ValueError("Mismatch between metadata and data length in EEGBlock")

        array = np.array(msg.data, dtype=np.float32)
        return array.reshape((msg.num_channels, msg.num_samples))