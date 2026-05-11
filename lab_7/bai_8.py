n = int(input("n = "))
stock = {}
prices = {}

for _ in range(n):
    name = input("item = ")
    stock[name] = int(input("stock = "))
    prices[name] = float(input("price = "))

total = 0

for name in sorted(stock):
    cost = stock[name] * prices[name]
    total += cost
    print(name, stock[name], prices[name], cost)

print("total =", total)
