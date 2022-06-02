import requests

get_first = input("Enter first currency: ").upper()
get_second = input("Enter second currency: ").upper()
get_amount = int(input("Enter amount: "))

if get_first != "" or get_second != "":
    result = requests.get(
        "http://data.fixer.io/api/latest?access_key=<YOUR-API-KEY>")

    first_rate = result.json()['rates'][get_first]
    second_rate = result.json()['rates'][get_second]

    print(
        f"{get_amount} {get_second} equals to {first_rate/second_rate * get_amount} {get_first}")
