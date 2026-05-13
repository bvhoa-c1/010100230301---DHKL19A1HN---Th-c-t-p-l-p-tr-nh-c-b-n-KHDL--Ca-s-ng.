n = int(input("Nhập số lượng phần tử: "))
arr = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(num)

even_numbers = list(filter(lambda x: x % 2 == 0, arr))
odd_numbers = list(filter(lambda x: x % 2 != 0, arr))

even_cubed = list(map(lambda x: x ** 3, even_numbers))
odd_squared = list(map(lambda x: x ** 2, odd_numbers))

print(f"\nMảng gốc: {arr}")
print(f"Nhóm số chẵn: {even_numbers}")
print(f"Nhóm số chẵn lập phương: {even_cubed}")
print(f"Nhóm số lẻ: {odd_numbers}")
print(f"Nhóm số lẻ bình phương: {odd_squared}")
