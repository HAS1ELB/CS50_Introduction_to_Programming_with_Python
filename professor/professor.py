import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        attempt = 0

        while attempt < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == result:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
            except ValueError:
                print("EEE")
                attempt += 1

        if attempt == 3:
            print(f"{x} + {y} = {result}")

    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
