# Bài 6.1: Phân loại số chẵn và lẻ, tính tổng từng nhóm

n = int(input("Nhập số phần tử của mảng: "))
arr = []

print("Nhập các số nguyên dương:")
for i in range(n):
    num = int(input(f"Phần tử {i+1}: "))
    arr.append(num)

even_sum = 0
odd_sum = 0
even_numbers = []
odd_numbers = []

for num in arr:
    if num % 2 == 0:
        even_numbers.append(num)
        even_sum += num
    else:
        odd_numbers.append(num)
        odd_sum += num

print(f"\nMảng nhập vào: {arr}")
print(f"Số chẵn: {even_numbers} - Tổng: {even_sum}")
print(f"Số lẻ: {odd_numbers} - Tổng: {odd_sum}")
