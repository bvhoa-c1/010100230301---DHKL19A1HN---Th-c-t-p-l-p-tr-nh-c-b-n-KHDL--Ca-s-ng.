so_luong = int(input("Nhap n: "))

fibonacci = [0, 1]

for i in range(2, so_luong):
    so_moi = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(so_moi)

print(fibonacci[:so_luong])