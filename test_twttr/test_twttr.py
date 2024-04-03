from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("22") == "22"

if __name__ == "__main__":
    main()
