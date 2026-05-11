# Tính hóa đơn chi tiết

stock = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

price = {
    "apple": 2,
    "banana": 1,
    "orange": 3
}

total = 0

for item in stock:
    cost = stock[item] * price[item]
    total += cost

    print(item)
    print("Số lượng:", stock[item])
    print("Đơn giá:", price[item])
    print("Thành tiền:", cost)
    print()

print("Tổng hóa đơn:", total)