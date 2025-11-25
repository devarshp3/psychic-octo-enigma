"""Small runner for the `psychic_calculator` package.

Usage:
    python scripts/run_calculator.py

This script exercises the public functions and prints results.
"""
from __future__ import annotations

from psychic_calculator import add, subtract, multiply, divide


def main() -> None:
    examples = [
        ("add", 1, 2, add),
        ("add", 1.5, 2.5, add),
        ("subtract", 5, 3, subtract),
        ("multiply", 2, 3, multiply),
        ("divide", 6, 3, divide),
    ]

    for name, a, b, fn in examples:
        try:
            result = fn(a, b)
            print(f"{name}({a}, {b}) -> {result}")
        except Exception as exc:  # pragma: no cover - demo only
            print(f"{name}({a}, {b}) -> error: {exc}")


if __name__ == "__main__":
    main()
