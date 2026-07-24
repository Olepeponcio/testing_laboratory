from testing_lab.core import normalize_file
from testing_lab.core import build_user_response
from testing_lab.core import process_user_status


def test_normalize_file_integrates_with_file_system(tmp_path):
    source = tmp_path / "input.txt"
    destination = tmp_path / "output.txt"
    source.write_text("  HoLa  ", encoding="utf-8")

    result = normalize_file(source, destination)

    assert result == destination
    assert destination.read_text(encoding="utf-8") == "hola"


def test_build_user_response_respects_contract():
    response = build_user_response(7, "active")

    assert set(response) == {"id", "status"}
    assert response["id"] == 7
    assert response["status"] == "active"


def test_process_user_status_end_to_end(tmp_path):
    source = tmp_path / "status.txt"
    destination = tmp_path / "normalized_status.txt"
    source.write_text("  AcTiVe  ", encoding="utf-8")

    response = process_user_status(source, destination, 7)

    assert response == {
        "id": 7,
        "status": "active",
    }
    assert destination.read_text(encoding="utf-8") == "active"
