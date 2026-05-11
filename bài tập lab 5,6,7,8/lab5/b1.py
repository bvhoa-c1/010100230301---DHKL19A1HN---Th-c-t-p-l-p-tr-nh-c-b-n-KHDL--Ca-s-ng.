n = int(input("Nhập số nguyên dương: "))
binary = ""
if n == 0:
    binary = "0"
else:
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
print("Dạng nhị phân:", binary)