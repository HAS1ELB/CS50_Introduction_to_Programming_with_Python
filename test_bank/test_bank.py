from bank import value
def main():
    test_value1()
    test_value2()
    test_value3()


def test_value1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello") == 0
def test_value2():
    assert value("hi") == 20
def test_value3():
    assert value("adam") == 100

if __name__ == "__main__":
    main()
