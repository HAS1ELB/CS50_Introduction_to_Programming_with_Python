def main():
    answer = input("Greeting: ")
    value = value(answer)
    print("$" + value)


def value(greeting):
    new_answer = greeting.lower().strip()

    if "hello" in new_answer:
        return 0
    elif "h" == new_answer[0]:
        return 20
    else :
        return 100


if __name__ == "__main__":
    main()
