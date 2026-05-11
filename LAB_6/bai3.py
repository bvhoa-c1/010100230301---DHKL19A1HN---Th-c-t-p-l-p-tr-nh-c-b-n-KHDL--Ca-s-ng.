n = int(input("Nhap so phan tu: "))

a = []

for i in range(n):
    x = float(input())
    a.append(x)

print("Gia tri lon nhat:", max(a))
print("Gia tri nho nhat:", min(a))