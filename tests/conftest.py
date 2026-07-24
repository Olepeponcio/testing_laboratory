import pytest


@pytest.fixture(scope="module")
def shared_values():
    return (" A ", " B ")
