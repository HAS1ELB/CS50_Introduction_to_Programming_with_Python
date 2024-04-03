def main():
    num = input("Fraction: ")
    p = convert(num)
    print(gauge(p))


def convert(num):
    while True:
        index = num.find("/")
        try:
            x = int(num[:index])
            y = int(num[index+1:])
            f = x / y
            if x > y:
                num = input("Fraction: ")
                continue
            else:
                p = int(f * 100)
                return p
        except (ValueError, ZeroDivisionError):
            raise




def gauge(p):
    if p >= 99:
        return "F"
    elif p <= 1:
        return "E"
    else:
        return str(p) + "%"


if __name__ == "__main__":
    main()
