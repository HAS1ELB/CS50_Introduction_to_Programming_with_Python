

def main():
    answer = input("Greeting: ")
    value(answer)


def value(greeting):
    new_answer = greeting.lower().strip()

    if "hello" in new_answer:
        print("$0")
    elif "h" == new_answer[0]:
        print("$20")
    else :
        print("$100")


if __name__ == "__main__":
    main()
