import pytest
from eeg_bridge.test import ros2_mock

@pytest.fixture(autouse=True, scope="session")
def apply_mocks():
    pass
