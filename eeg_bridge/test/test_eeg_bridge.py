import numpy as np
import pytest

from std_msgs.msg import Header
from builtin_interfaces.msg import Time

from eeg_bridge.bridge import EEGBridge


def test_numpy_to_eegblock_and_back():
    num_channels = 4
    num_samples = 10
    sampling_rate = 128.0
    rng = np.random.default_rng(seed=42)
    data = rng.random((num_channels, num_samples), dtype=np.float32)

    header = Header(stamp=Time(sec=123, nanosec=456))

    eeg_msg = EEGBridge.numpy_to_eegblock(
        data,
        sampling_rate=sampling_rate,
        header=header
    )

    assert eeg_msg.num_channels == num_channels
    assert eeg_msg.num_samples == num_samples
    assert eeg_msg.sampling_rate == sampling_rate
    assert len(eeg_msg.data) == num_channels * num_samples
    assert eeg_msg.header.stamp.sec == 123
    assert eeg_msg.header.stamp.nanosec == 456

    result = EEGBridge.eegblock_to_numpy(eeg_msg)

    assert result.shape == (num_channels, num_samples)
    np.testing.assert_array_almost_equal(result, data)