# Phân loại số chẵn và số lẻ trong mảng

n = int(input("Nhập số lượng phần tử: "))

arr = []

# Nhập mảng
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(x)

even_numbers = []
odd_numbers = []

sum_even = 0
sum_odd = 0

# Phân loại và tính tổng
for num in arr:

    if num % 2 == 0:
        even_numbers.append(num)
        sum_even += num
    else:
        odd_numbers.append(num)
        sum_odd += num

# Hiển thị kết quả
print("Danh sách số chẵn:", even_numbers)
print("Tổng số chẵn:", sum_even)

print("Danh sách số lẻ:", odd_numbers)
print("Tổng số lẻ:", sum_odd)