while True:
    fuel = input("Fraction: ")
    try:
        numerator, denominator = fuel.split("/")
        new_num = int(numerator)
        new_den = int(denominator)
        f = new_num / new_den
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

p = round(f * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
