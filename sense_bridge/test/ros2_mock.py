import sys
import types

# Mock builtin_interfaces.msg.Time 
builtin_interfaces = types.ModuleType("builtin_interfaces")
builtin_msg = types.ModuleType("msg")

class Time:
    def __init__(self, sec=0, nanosec=0):
        self.sec = sec
        self.nanosec = nanosec

builtin_msg.Time = Time
builtin_interfaces.msg = builtin_msg
sys.modules["builtin_interfaces"] = builtin_interfaces
sys.modules["builtin_interfaces.msg"] = builtin_msg

# Mock std_msgs.msg.Header
std_msgs = types.ModuleType("std_msgs")
std_msg_msg = types.ModuleType("msg")

class Header:
    def __init__(self, stamp=None):
        self.stamp = stamp if stamp else Time()

std_msg_msg.Header = Header
std_msgs.msg = std_msg_msg
sys.modules["std_msgs"] = std_msgs
sys.modules["std_msgs.msg"] = std_msg_msg

# Mock sense_msgs.msg.EEGBlock
sense_msgs = types.ModuleType("sense_msgs")
sense_msg_msg = types.ModuleType("msg")

class EEGBlock:
    def __init__(self):
        self.header = Header()
        self.num_channels = 0
        self.num_samples = 0
        self.sampling_rate = 0.0
        self.data = []

sense_msg_msg.EEGBlock = EEGBlock
sense_msgs.msg = sense_msg_msg
sys.modules["sense_msgs"] = sense_msgs
sys.modules["sense_msgs.msg"] = sense_msg_msg

# Mock rclpy and rclpy.time
rclpy = types.ModuleType("rclpy")
rclpy_time = types.ModuleType("rclpy.time")

class RclpyTime:
    def __init__(self, seconds=0.0):
        self.seconds = seconds

rclpy_time.Time = RclpyTime
sys.modules["rclpy"] = rclpy
sys.modules["rclpy.time"] = rclpy_time
