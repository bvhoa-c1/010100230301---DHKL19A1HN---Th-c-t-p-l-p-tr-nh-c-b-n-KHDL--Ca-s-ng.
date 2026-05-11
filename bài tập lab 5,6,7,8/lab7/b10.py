warehouse = set()
customer_bought = set()
n = int(input("Số sản phẩm trong kho: "))
for i in range(n):
    warehouse.add(input("Sản phẩm: "))
m = int(input("Số sản phẩm khách mua: "))
for i in range(m):
    customer_bought.add(input("Khách mua: "))
unsold = warehouse - customer_bought
print("Hàng chưa bán:", unsold)