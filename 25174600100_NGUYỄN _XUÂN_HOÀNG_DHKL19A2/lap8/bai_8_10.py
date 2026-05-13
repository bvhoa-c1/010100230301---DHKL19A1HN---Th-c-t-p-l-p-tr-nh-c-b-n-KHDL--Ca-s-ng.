# Bài 8.10: Kết hợp map và filter - lập phương cho số chẵn, bình phương cho số lẻ

# Tạo mảng hỗn hợp
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Mảng gốc:")
print(numbers)

# Cách 1: Sử dụng filter và map riêng biệt
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))

cubed_evens = list(map(lambda x: x**3, evens))
squared_odds = list(map(lambda x: x**2, odds))

print("\nSố chẵn:", evens)
print("Lập phương của số chẵn:", cubed_evens)

print("\nSố lẻ:", odds)
print("Bình phương của số lẻ:", squared_odds)

# Cách 2: Kết hợp filter + map trong một biểu thức
def process_number(x):
    if x % 2 == 0:
        return x ** 3
    else:
        return x ** 2

result = list(map(process_number, numbers))

print("\nKết hợp map + filter (lập phương chẵn, bình phương lẻ):")
print(result)

# Cách 3: Hiển thị chi tiết
print("\n" + "=" * 60)
print(f"{'Số':<5} {'Loại':<10} {'Phép toán':<15} {'Kết quả':<10}")
print("-" * 60)

for num, res in zip(numbers, result):
    if num % 2 == 0:
        loai = "Chẵn"
        phep = f"{num}³"
    else:
        loai = "Lẻ"
        phep = f"{num}²"
    
    print(f"{num:<5} {loai:<10} {phep:<15} {res:<10}")

# Tính tổng
print("-" * 60)
print(f"Tổng kết quả: {sum(result)}")

# Nhập mảng từ người dùng
print("\n" + "=" * 60)
try:
    user_input = input("Nhập các số (cách nhau bởi dấu cách): ")
    arr = list(map(int, user_input.split()))
    
    results = list(map(process_number, arr))
    
    print(f"\nMảng gốc: {arr}")
    print(f"Kết quả (³ cho chẵn, ² cho lẻ): {results}")
    print(f"Tổng: {sum(results)}")
    
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ!")
