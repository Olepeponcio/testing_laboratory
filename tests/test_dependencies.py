from testing_lab.core import get_user_status
from testing_lab.core import get_execution_mode
from testing_lab.core import register_user


def test_get_user_status_returns_external_status():
    def status_stub(user_id):
        return "active"

    result = get_user_status(7, status_stub)

    assert result == "active"


def test_get_user_status_passes_user_id_to_service():
    received_ids = []

    def status_spy(user_id):
        received_ids.append(user_id)
        return "active"

    result = get_user_status(7, status_spy)

    assert result == "active"
    assert received_ids == [7]


from unittest.mock import Mock


def test_get_user_status_calls_service_with_user_id():
    status_mock = Mock(return_value="active")

    result = get_user_status(7, status_mock)

    assert result == "active"
    status_mock.assert_called_once_with(7)


def test_get_execution_mode_uses_environment_variable(monkeypatch):
    monkeypatch.setenv("APP_MODE", "testing")

    result = get_execution_mode()

    assert result == "testing"


class FakeUserRepository:
    def __init__(self):
        self.users = set()

    def exists(self, user_id):
        return user_id in self.users

    def save(self, user_id):
        self.users.add(user_id)


def test_register_user_saves_new_user():
    repository = FakeUserRepository()

    result = register_user(7, repository)

    assert result is True
    assert repository.exists(7)


def test_register_user_rejects_existing_user():
    repository = FakeUserRepository()
    repository.save(7)

    result = register_user(7, repository)

    assert result is False
    assert repository.users == {7}
