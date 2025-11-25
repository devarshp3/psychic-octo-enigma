import pytest

from psychic_calculator import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3.0),
        (1.5, 2.5, 4.0),
        (-1, 1, 0.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2.0),
        (2.5, 1.0, 1.5),
        (0, 0, 0.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6.0),
        (1.5, 2, 3.0),
        (0, 5, 0.0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


def test_divide_success():
    assert divide(6, 3) == 2.0


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
