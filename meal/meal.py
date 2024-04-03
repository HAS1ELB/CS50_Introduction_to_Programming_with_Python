def main():

    time = input("What time is it? ")

    time_float = convert(time)

    if 7 <= time_float <= 8:
        print("breakfast time")
    if 12 <= time_float <= 13:
        print("lunch time")
    if 18 <= time_float <=19:
        print("dinner time")


def convert(time):
    hours, minutes= time.split(":")
    new_min = float(minutes) / 60
    return float(hours) + new_min

if __name__ == "__main__":
    main()

