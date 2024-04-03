from seasons import minutes_lived

def main():
    test1()
    test2()

def test1():
    assert minutes_lived(2003, 5, 17) == "Ten million, nine hundred fifty-six thousand, nine hundred sixty minutes"
    assert minutes_lived(2000, 2, 1) == "Twelve million, six hundred eighty-six thousand, four hundred minutes"


def test2():
    assert minutes_lived(23, 1, 20001) == "Invalid Date"

if __name__ == "__main__":
    main()
