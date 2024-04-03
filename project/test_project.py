from project import add, subtract, multiply, divide


def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(2.5, 2.5) == 5


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(10, 7) == 3


def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 4) == 10


def test_divide():
    assert divide(10, 2) == 5
    assert divide(8, 4) == 2
    assert divide(5, 0) == "Cannot divide by zero"
