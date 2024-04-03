from um import count

def main():
    test1()
    test2()
    test3()

def test1():
    assert count("um") == 1
def test2():
    assert count("um ,um .um yummy") == 3
def test3():
    assert count("Um") == 1
    assert count("ghv") == 0

if __name__ == "__main__":
    main()
