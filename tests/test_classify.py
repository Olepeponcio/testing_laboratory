from testing_lab.core import classify_score


def test_score_zero_is_insufficient():
    assert classify_score(0) == "insuficiente"


def test_score_49_is_insufficient():
    assert classify_score(49) == "insuficiente"


def test_score_50_is_passed():
    assert classify_score(50) == "aprobado"


def test_score_69_is_passed():
    assert classify_score(69) == "aprobado"


def test_score_70_is_notable():
    assert classify_score(70) == "notable"


def test_score_89_is_notable():
    assert classify_score(89) == "notable"


def test_score_90_is_excellent():
    assert classify_score(90) == "excelente"


def test_score_100_is_excellent():
    assert classify_score(100) == "excelente"