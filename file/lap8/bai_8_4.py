# Bài 8.4: Hàm cubesum - tính tổng các lập phương của chữ số

def cubesum(n):
    """Tính tổng các lập phương của các chữ số trong n"""
    n = abs(n)  # Lấy giá trị tuyệt đối
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    
    return total

# Kiểm tra hàm
print("CubeSum - Tính tổng các lập phương của chữ số")
print("=" * 50)

test_numbers = [153, 370, 371, 407, 1, 2, 100, 999, 12345]

print(f"{'Số':<10} {'Các chữ số':<20} {'Lập phương':<30} {'Tổng':<10}")
print("-" * 70)

for num in test_numbers:
    digits = list(str(abs(num)))
    cubes = " + ".join([f"{d}³" for d in digits])
    result = cubesum(num)
    print(f"{num:<10} {', '.join(digits):<20} {cubes:<30} {result:<10}")

# Nhập từ người dùng
print("\n" + "=" * 50)
try:
    num = int(input("Nhập một số nguyên: "))
    result = cubesum(num)
    print(f"CubeSum({num}) = {result}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
