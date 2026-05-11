stock = {
    "apple": 5,
    "banana": 3,
    "milk": 2
}

price = {
    "apple": 10000,
    "banana": 5000,
    "milk": 30000
}

total = 0

print("HOA DON")

for item in stock:

    cost = stock[item] * price[item]
    total += cost

    print(item, ":", stock[item], "x",
          price[item], "=", cost)

print("Tong tien =", total)