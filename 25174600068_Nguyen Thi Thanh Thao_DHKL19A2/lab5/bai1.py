n = int(input("Nhap n: "))

binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = n // 2

print(binary)