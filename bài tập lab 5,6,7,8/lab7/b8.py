stock = {}
price = {}
n = int(input("Số mặt hàng: "))
for i in range(n):
    item = input("Tên hàng: ")
    stock[item] = int(input("Số lượng: "))
    price[item] = int(input("Đơn giá: "))
total = 0
for item in stock:
    total += stock[item] * price[item]
print("Tổng tiền:", total)