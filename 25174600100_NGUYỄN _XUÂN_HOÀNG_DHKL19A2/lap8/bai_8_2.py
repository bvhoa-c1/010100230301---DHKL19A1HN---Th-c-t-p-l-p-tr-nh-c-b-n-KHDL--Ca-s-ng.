# Bài 8.2: Hàm tính giai thừa

def factorial(n):
    """Tính giai thừa của n (n!)"""
    if n < 0:
        raise ValueError("Giai thừa không xác định cho số âm!")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Kiểm tra hàm
print("Bảng giai thừa:")
print("-" * 30)
print(f"{'n':<5} {'n!':<15}")
print("-" * 30)

for n in range(0, 11):
    print(f"{n:<5} {factorial(n):<15}")

# Lấy đầu vào từ người dùng
print("\n" + "=" * 30)
try:
    num = int(input("Nhập một số nguyên dương: "))
    result = factorial(num)
    print(f"{num}! = {result}")
except ValueError as e:
    print(f"Lỗi: {e}")
except Exception as e:
    print(f"Lỗi: {e}")
