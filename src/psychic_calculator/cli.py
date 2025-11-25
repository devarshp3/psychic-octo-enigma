"""CLI for the `psychic_calculator` package.

Provides a small command-line interface that performs basic arithmetic.
"""
from __future__ import annotations

import argparse
import sys
from typing import Sequence

from .calculator import add, subtract, multiply, divide


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="psychic-calculator")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="operation")
    parser.add_argument("a", type=float, help="first operand")
    parser.add_argument("b", type=float, help="second operand")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for the CLI; returns exit code (0 on success)."""
    argv = list(argv) if argv is not None else None
    parser = build_parser()
    args = parser.parse_args(argv)

    ops = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide,
    }

    fn = ops[args.operation]
    try:
        result = fn(args.a, args.b)
    except Exception as exc:
        print(f"error: {exc}")
        return 2

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
