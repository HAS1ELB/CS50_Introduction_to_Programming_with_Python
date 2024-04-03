from validator_collection import checkers

def main():
    print(response(input("Text: ")))


def response(n):

    if checkers.is_email(n):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
