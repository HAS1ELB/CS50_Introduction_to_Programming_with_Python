from numb3rs import validate

def main():
    test_ip_true()
    test_ip_false()

def test_ip_true():
    assert validate("215.215.215.215") == True
    assert validate("12.3.154.34") == True
def test_ip_false():
    assert validate("Raja") == False
    assert validate("1.256.256.257") == False
    assert validate("1245.26.250.135") == False

if __name__ == "__main__":
    main()
