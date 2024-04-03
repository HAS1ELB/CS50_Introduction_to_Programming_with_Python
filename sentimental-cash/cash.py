from cs50 import get_float

while True:
    dollars = get_float("Change Owed: ")
    if dollars >= 0:
        break

cents = round(dollars * 100)
coins = 0
den = [25,10,5,1]

for d in den:
    coins += cents // d
    cents %= d


print(coins)

