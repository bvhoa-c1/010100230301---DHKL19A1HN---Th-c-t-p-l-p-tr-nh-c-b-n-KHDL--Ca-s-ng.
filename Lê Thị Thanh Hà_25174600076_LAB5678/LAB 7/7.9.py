inventory = {
    "Táo": 20,
    "Cam": 15,
    "Xoài": 10
}

sold = {
    "Táo": 5,
    "Cam": 3
}

for item, qty in sold.items():
    if item in inventory:
        inventory[item] -= qty

print("Tồn kho sau cập nhật:")
print(inventory)

