import requests
from sys import argv, exit

if len(argv) != 2:
    exit("Missing command-line argument")

try:
    btc_price = requests.get(
        "inser link here dot json"
    ).json()["bpi"]["USD"]["rate_float"]

    bitcoins = float(argv[1])

except (requests.RequestException, KeyError, ValueError):
    exit("Command-line argument is not a number")

print(f"${bitcoins * btc_price:,.4f}") 
