# Bài 7.8 + 7.9 gộp lại
# Khởi tạo tồn kho và đơn giá
stock = {}
price = {}

n = int(input("Số mặt hàng trong kho: "))
for i in range(n):
    item = input("Tên mặt hàng: ")
    stock[item] = int(input("Số lượng tồn: "))
    price[item] = int(input("Đơn giá: "))

# Bài 7.8: Tính tổng giá trị kho
total_value = 0
for item in stock:
    total_value += stock[item] * price[item]
print("Tổng giá trị kho:", total_value)

# Bài 7.9: Bán hàng và cập nhật kho
m = int(input("Số mặt hàng khách mua: "))
for i in range(m):
    item = input("Mặt hàng khách mua: ")
    qty = int(input("Số lượng mua: "))
    if item in stock and stock[item] >= qty:
        stock[item] -= qty
        print("Đã bán", qty, item)
    else:
        print("Không đủ hàng hoặc không có mặt hàng:", item)

print("Tồn kho sau khi bán:", stock)