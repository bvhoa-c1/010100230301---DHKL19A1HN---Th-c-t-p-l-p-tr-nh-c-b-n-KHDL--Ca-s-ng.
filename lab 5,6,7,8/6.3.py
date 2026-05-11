

n = int(input("Nhap so luong phan tu: "))

arr = []

for i in range(n):
    x = float(input(f"Nhap phan tu thu {i + 1}: "))
    arr.append(x)

print("Gia tri lon nhat:", max(arr))
print("Gia tri nho nhat:", min(arr))