def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_W = d.replace("$","")
    return float(d_W)

def percent_to_float(p):
    p_w = p.replace("%","")
    p_c = float(p_w)/100
    return p_c

main()
