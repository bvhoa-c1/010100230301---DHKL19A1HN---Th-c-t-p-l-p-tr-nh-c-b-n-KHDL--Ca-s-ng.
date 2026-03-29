n = int(input("Nhập n: "))
i = n // 2
while i >= 1:
    if n % i == 0:
        print(f"Ước số lớn nhất khác {n} là: {i}")
        break
    i -= 1