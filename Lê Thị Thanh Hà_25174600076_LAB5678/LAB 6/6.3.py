n = int(input("Nhập số lượng phần tử: "))

a = []

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

print("Giá trị lớn nhất:", max(a))
print("Giá trị nhỏ nhất:", min(a))