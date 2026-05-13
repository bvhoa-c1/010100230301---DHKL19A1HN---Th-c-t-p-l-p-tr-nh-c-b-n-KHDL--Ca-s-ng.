# Bài 8.9: Sử dụng map để tính lập phương của tất cả phần tử

# Tạo mảng
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Mảng gốc:")
print(numbers)

# Sử dụng map với lambda để tính lập phương
cubed = list(map(lambda x: x**3, numbers))

print("\nLập phương của mỗi phần tử (dùng map + lambda):")
print(cubed)

# Cách khác: định nghĩa hàm riêng
def cube(x):
    return x ** 3

cubed_func = list(map(cube, numbers))

print("\nLập phương của mỗi phần tử (dùng hàm cube):")
print(cubed_func)

# Cách khác: sử dụng List Comprehension
cubed_lc = [x**3 for x in numbers]

print("\nLập phương của mỗi phần tử (dùng List Comprehension):")
print(cubed_lc)

# Hiển thị chi tiết
print("\n" + "=" * 50)
print(f"{'Số':<10} {'Lập phương':<15}")
print("-" * 25)
for num, cube_num in zip(numbers, cubed):
    print(f"{num:<10} {cube_num:<15}")

# Nhập mảng từ người dùng
print("\n" + "=" * 50)
try:
    user_input = input("Nhập các số (cách nhau bởi dấu cách): ")
    arr = list(map(int, user_input.split()))
    
    cubes = list(map(lambda x: x**3, arr))
    
    print(f"\nMảng gốc: {arr}")
    print(f"Lập phương: {cubes}")
    print(f"Tổng lập phương: {sum(cubes)}")
    
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ!")
