"""Small calculator utilities used in examples and tests.

Functions use simple, well-typed signatures and raise standard exceptions for
error conditions (e.g., `ZeroDivisionError`). Keep implementations trivial
so unit tests can be precise and fast.
"""
from __future__ import annotations

import logging
from typing import Union

logger = logging.getLogger(__name__)

Number = Union[int, float]


def add(a: Number, b: Number) -> float:
    """Return the sum of two numbers as a float."""
    result = float(a) + float(b)
    logger.debug("add: %s + %s = %s", a, b, result)
    return result


def subtract(a: Number, b: Number) -> float:
    """Return the difference (a - b) as a float."""
    result = float(a) - float(b)
    logger.debug("subtract: %s - %s = %s", a, b, result)
    return result


def multiply(a: Number, b: Number) -> float:
    """Return the product of two numbers as a float."""
    result = float(a) * float(b)
    logger.debug("multiply: %s * %s = %s", a, b, result)
    return result


def divide(a: Number, b: Number) -> float:
    """Return the division a / b as a float.

    Raises:
        ZeroDivisionError: if `b` is zero.
    """
    if float(b) == 0.0:
        logger.warning("divide: division by zero attempted (%s / %s)", a, b)
        raise ZeroDivisionError("division by zero")
    result = float(a) / float(b)
    logger.debug("divide: %s / %s = %s", a, b, result)
    return result
