stock = {
    "apple": 10,
    "banana": 8,
    "milk": 5
}

sell = {
    "apple": 3,
    "milk": 2
}

for item in sell:

    if item in stock:
        stock[item] -= sell[item]

print("Ton kho sau giao dich:")

for k, v in stock.items():
    print(k, ":", v)