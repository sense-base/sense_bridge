import pytest
import test.ros2_mock

@pytest.fixture(autouse=True, scope="session")
def apply_mocks():
    pass