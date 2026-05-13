n = int(input("Nhập số lượng phần tử trong mảng: "))
arr = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(num)

even_sum = 0
odd_sum = 0
even_list = []
odd_list = []

for num in arr:
    if num % 2 == 0:
        even_sum += num
        even_list.append(num)
    else:
        odd_sum += num
        odd_list.append(num)

print(f"\nMảng gốc: {arr}")
print(f"Nhóm số chẵn: {even_list}")
print(f"Tổng số chẵn: {even_sum}")
print(f"Nhóm số lẻ: {odd_list}")
print(f"Tổng số lẻ: {odd_sum}")
