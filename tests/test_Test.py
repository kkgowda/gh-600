import importlib
import sys


def test_sum():
    from Test import sum

    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0


def test_print_on_import(capsys):
    # Ensure a fresh import so the top-level print in Test.py runs during the test
    if 'Test' in sys.modules:
        del sys.modules['Test']

    importlib.import_module('Test')
    captured = capsys.readouterr()
    assert 'Hello world' in captured.out
