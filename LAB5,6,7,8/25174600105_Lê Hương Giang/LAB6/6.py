n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = int(input("Nhập số: "))
    a.append(x)
hieu = a[1] - a[0]
for i in range(1, n - 1):
    if a[i+1] - a[i] != hieu:
        print("Không phải cấp số cộng")
        break
else:
    print("Là cấp số cộng")