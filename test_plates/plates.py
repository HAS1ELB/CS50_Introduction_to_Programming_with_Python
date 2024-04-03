def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False

    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    if not plate.isalnum():
        return False

    number_found = False
    for char in plate:
        if char.isdigit():
            number_found = True
            if char == '0' and plate.index(char) == 2:
                return False
        elif number_found:
            return False

    return True


if __name__ == "__main__":
    main()
