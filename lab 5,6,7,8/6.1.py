

n = int(input("Nhap so luong phan tu: "))

arr = []

for i in range(n):
    x = int(input(f"Nhap phan tu thu {i + 1}: "))
    arr.append(x)

even = []
odd = []

for x in arr:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

print("Danh sach so chan:", even)
print("Tong chan:", sum(even))

print("Danh sach so le:", odd)
print("Tong le:", sum(odd))