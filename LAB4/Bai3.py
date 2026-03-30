n = int(input("Nhập n: "))
max_div = 1
for i in range(1, n):
    if n % i == 0:
        max_div = i
print(f"Ước số lớn nhất khác {n} là {max_div}")
