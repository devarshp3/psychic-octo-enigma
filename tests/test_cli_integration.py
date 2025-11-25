import subprocess
import sys


def run_module(args):
    cmd = [sys.executable, "-m", "psychic_calculator.cli"] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def test_cli_add_module():
    res = run_module(["add", "1", "2"])
    assert res.returncode == 0
    assert res.stdout.strip() == "3.0"


def test_cli_divide_by_zero_module():
    res = run_module(["div", "1", "0"])
    assert res.returncode == 2
    assert res.stdout.startswith("error:")
