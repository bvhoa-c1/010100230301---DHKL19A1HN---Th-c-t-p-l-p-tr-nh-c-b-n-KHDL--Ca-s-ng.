n = int(input("number of stock items = "))
stock = {}

for _ in range(n):
    name = input("item = ")
    stock[name] = int(input("stock = "))

m = int(input("number of sold items = "))

for _ in range(m):
    name = input("sold item = ")
    quantity = int(input("quantity = "))
    if name in stock and stock[name] >= quantity:
        stock[name] -= quantity
        print(name, "success")
    else:
        print(name, "failed")

for name in sorted(stock):
    print(name, stock[name])
