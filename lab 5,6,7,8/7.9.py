# Cập nhật tồn kho sau giao dịch

stock = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

sold = {
    "apple": 3,
    "banana": 2
}

for item in sold:
    if item in stock:
        stock[item] -= sold[item]

print("Tồn kho cập nhật:")
print(stock)