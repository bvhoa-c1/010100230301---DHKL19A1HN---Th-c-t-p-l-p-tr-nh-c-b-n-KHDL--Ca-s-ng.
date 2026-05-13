n = int(input("Nhập số lượng phần tử: "))
arr = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(num)

cubed = list(map(lambda x: x ** 3, arr))

print(f"\nMảng gốc: {arr}")
print(f"Mảng lập phương: {cubed}")
