import io
import sys

from psychic_calculator import cli


def run_cli(args):
    # Capture stdout
    old_stdout = sys.stdout
    try:
        sys.stdout = io.StringIO()
        exit_code = cli.main(args)
        output = sys.stdout.getvalue().strip()
    finally:
        sys.stdout = old_stdout
    return exit_code, output


def test_cli_add():
    rc, out = run_cli(["add", "1", "2"])
    assert rc == 0
    assert out == "3.0"


def test_cli_divide_by_zero():
    rc, out = run_cli(["div", "1", "0"])
    assert rc == 2
    assert out.startswith("error:")
