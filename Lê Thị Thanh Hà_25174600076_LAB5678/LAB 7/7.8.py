products = {
    "Táo": {"quantity": 10, "price": 5},
    "Cam": {"quantity": 8, "price": 6},
    "Xoài": {"quantity": 5, "price": 12}
}

total = 0
print("Chi tiết hóa đơn:")

for name, info in products.items():
    cost = info["quantity"] * info["price"]
    total += cost

    print(name, ":", cost)

print("Tổng tiền:", total)


