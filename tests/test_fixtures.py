import pytest

from testing_lab.core import normalize_text


@pytest.fixture
def sample_values():
    return [" A ", " B "]


def test_normalizes_values_from_fixture(sample_values):
    results = [normalize_text(value) for value in sample_values]

    assert results == ["a", "b"]


def test_fixture_starts_with_fresh_values(sample_values):
    sample_values.append(" C ")

    assert sample_values == [" A ", " B ", " C "]


@pytest.fixture
def text_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("  Hola  ", encoding="utf-8")

    yield file_path

    file_path.unlink()


def test_normalizes_text_from_file(text_file):
    raw_text = text_file.read_text(encoding="utf-8")

    assert normalize_text(raw_text) == "hola"


@pytest.fixture(scope="module")
def shared_values():
    return (" A ", " B ")


def test_module_fixture_normalizes_first_value(shared_values):
    assert normalize_text(shared_values[0]) == "a"


def test_module_fixture_normalizes_second_value(shared_values):
    assert normalize_text(shared_values[1]) == "b"
