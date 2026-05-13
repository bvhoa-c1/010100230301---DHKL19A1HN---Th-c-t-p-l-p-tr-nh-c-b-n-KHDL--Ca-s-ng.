n = int(input("Nhập số lượng phần tử: "))
arr = []

for i in range(n):
    num = float(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(num)

max_val = max(arr)
min_val = min(arr)

print(f"\nDãy số: {arr}")
print(f"Giá trị lớn nhất: {max_val}")
print(f"Giá trị nhỏ nhất: {min_val}")
