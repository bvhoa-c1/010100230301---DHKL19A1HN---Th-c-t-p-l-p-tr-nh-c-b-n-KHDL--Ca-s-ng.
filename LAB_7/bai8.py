quantity = {
    "Pen": 10,
    "Book": 5,
    "Bag": 2
}

price = {
    "Pen": 5000,
    "Book": 20000,
    "Bag": 150000
}

total = 0

print("HOA DON")

for item in quantity:
    cost = quantity[item] * price[item]
    total += cost

    print(item, "-", quantity[item], "-", price[item], "-", cost)

print("Tong tien:", total)