import pytest
from testing_lab.core import classify_score

# def test_score_zero_is_insufficient():
#     assert classify_score(0) == "insuficiente"


# def test_score_49_is_insufficient():
#     assert classify_score(49) == "insuficiente"


# def test_score_50_is_passed():
#     assert classify_score(50) == "aprobado"


# def test_score_69_is_passed():
#     assert classify_score(69) == "aprobado"


# def test_score_70_is_notable():
#     assert classify_score(70) == "notable"


# def test_score_89_is_notable():
#     assert classify_score(89) == "notable"


# def test_score_90_is_excellent():
#     assert classify_score(90) == "excelente"


# def test_score_100_is_excellent():
#     assert classify_score(100) == "excelente"


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (0, "insuficiente"),
        (49, "insuficiente"),
        (50, "aprobado"),
        (69, "aprobado"),
        (70, "notable"),
        (89, "notable"),
        (90, "excelente"),
        (100, "excelente"),
    ],
)
def test_classify_score(score, expected):
    assert classify_score(score) == expected


def test_classify_score_rejects_value_below_minimum():
    with pytest.raises(ValueError):
        classify_score(-1)


def test_classify_score_rejects_value_above_maximum():
    with pytest.raises(ValueError):
        classify_score(101)


@pytest.mark.parametrize("invalid_score", ["50", None, 50.5, True])
def test_classify_score_rejects_non_integer_values(invalid_score):
    with pytest.raises(
        TypeError,
        match="score must be an integer",
    ):
        classify_score(invalid_score)
