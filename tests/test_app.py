from src.app import add


def test_add_basic():
    assert add(2, 3) == 6


def test_add_zero():
    assert add(0, 0) == 0
