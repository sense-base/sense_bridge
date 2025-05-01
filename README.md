# sense_bridge

`sense_bridge` is a ROS 2 (Humble) package that provides utility functions to convert between NumPy arrays and custom `EEGBlock` messages defined in [`sense_msgs`](https://github.com/your-org/sense_msgs). It enables interoperability between typical scientific Python workflows and real-time ROS 2 EEG pipelines.

## Features

- Convert EEG data from NumPy arrays to `EEGBlock` messages and vice versa.
- Ensures compatibility with the `sense_eeg` publisher and downstream ROS 2 nodes.

