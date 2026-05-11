n = int(input("Nhập số phần tử: "))
a = []
for i in range(n):
    x = float(input("Nhập số: "))
    a.append(x)
print("Số lớn nhất:", max(a))
print("Số nhỏ nhất:", min(a))