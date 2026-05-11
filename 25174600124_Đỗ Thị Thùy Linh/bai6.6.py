n = int(input("Nhap n: "))

a = []

for i in range(n):
    a.append(int(input()))

d = a[1] - a[0]

check = True

for i in range(1, n - 1):
    if a[i + 1] - a[i] != d:
        check = False
        break

if check:
    print("Day la cap so cong")
else:
    print("Khong phai cap so cong")