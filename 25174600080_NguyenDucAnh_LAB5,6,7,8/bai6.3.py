# Tìm giá trị lớn nhất và nhỏ nhất trong dãy số

n = int(input("Nhập số lượng phần tử: "))

arr = []

# Nhập dãy số
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(x)

# Gán giá trị đầu tiên
max_value = arr[0]
min_value = arr[0]

# Tìm max và min
for num in arr:

    if num > max_value:
        max_value = num

    if num < min_value:
        min_value = num

# Hiển thị kết quả
print("Giá trị lớn nhất là:", max_value)
print("Giá trị nhỏ nhất là:", min_value)