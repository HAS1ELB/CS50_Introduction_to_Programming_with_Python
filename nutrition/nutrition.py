def get_fruit_calories(fruit):
    fruit_calories = {
        "APPLE": 130,
        "AVOCADO": 50,
        "BANANA": 110,
        "CANTAKOUPE": 50,
        "GRAPEFRUIT": 60,
        "GRAPES": 90,
        "HONEYDEW MELON": 50,
        "KIWIFRUIT": 90,
        "LEMON": 15,
        "LIME": 20,
        "NECTARINE": 60,
        "ORANGE": 80,
        "PEACH": 60,
        "PEAR": 100,
        "PINEAPPLE": 50,
        "PLUMS": 70,
        "STRAWBERRIES": 50,
        "SWEET CHERRIES": 100,
        "TANGERINE": 50,
        "WATERMELON": 80
    }

    fruit = fruit.upper()
    if fruit in fruit_calories:
        return fruit_calories[fruit]
    else:
        return None

def main():
    fruit = input("Enter a fruit: ").upper()
    calories = get_fruit_calories(fruit)

    if calories is not None:
        print(f"One portion of {fruit.capitalize()} contains {calories} calories.")
    else:
        print("")

if __name__ == "__main__":
    main()
