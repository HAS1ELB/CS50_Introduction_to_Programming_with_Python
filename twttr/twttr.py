def main():
    answer = input("Input: ")
    print(shorten(answer))


def shorten(word):
    txt = ""
    for l in word:
        if l not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            txt += l
    return txt


if __name__ == "__main__":
    main()
