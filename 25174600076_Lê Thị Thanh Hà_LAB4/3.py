n = int(input("Nhập n: "))

for i in range(n - 1, 0, -1):
    if n % i == 0:
        print("Ước lớn nhất (khác n):", i)
        break