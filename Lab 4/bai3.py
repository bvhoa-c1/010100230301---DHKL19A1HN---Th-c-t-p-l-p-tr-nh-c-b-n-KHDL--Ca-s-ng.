n = int(input("Nhập n: "))
i = n - 1

while i > 0:
    if n % i == 0:
        print("Ước lớn nhất (khác n) là:", i)
        break
    i -= 1
    