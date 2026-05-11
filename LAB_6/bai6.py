n = int(input("Nhap so phan tu: "))

a = []

for i in range(n):
    a.append(int(input()))

hieu = []

for i in range(1, n):
    hieu.append(a[i] - a[i - 1])

print("Sai phan:", hieu)

if len(set(hieu)) == 1:
    print("Day la cap so cong")
else:
    print("Khong phai cap so cong")