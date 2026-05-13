# Bài 8.8: Sử dụng filter và lambda để tách số chẵn và lẻ

# Tạo mảng hỗn hợp
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40]

print("Mảng gốc:")
print(numbers)

# Sử dụng filter và lambda để tách số chẵn
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Sử dụng filter và lambda để tách số lẻ
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("\nSố chẵn (dùng filter + lambda):")
print(even_numbers)

print("\nSố lẻ (dùng filter + lambda):")
print(odd_numbers)

# Cách khác: sử dụng List Comprehension
even_lc = [x for x in numbers if x % 2 == 0]
odd_lc = [x for x in numbers if x % 2 != 0]

print("\nSố chẵn (dùng List Comprehension):")
print(even_lc)

print("\nSố lẻ (dùng List Comprehension):")
print(odd_lc)

# Nhập mảng từ người dùng
print("\n" + "=" * 50)
try:
    user_input = input("Nhập các số (cách nhau bởi dấu cách): ")
    arr = list(map(int, user_input.split()))
    
    evens = list(filter(lambda x: x % 2 == 0, arr))
    odds = list(filter(lambda x: x % 2 != 0, arr))
    
    print(f"\nMảng: {arr}")
    print(f"Số chẵn: {evens}")
    print(f"Số lẻ: {odds}")
    print(f"Tổng số chẵn: {sum(evens)}")
    print(f"Tổng số lẻ: {sum(odds)}")
    
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ!")
