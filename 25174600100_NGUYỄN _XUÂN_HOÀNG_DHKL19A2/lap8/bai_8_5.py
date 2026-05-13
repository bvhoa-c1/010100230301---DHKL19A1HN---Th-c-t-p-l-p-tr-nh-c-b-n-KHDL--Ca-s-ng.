# Bài 8.5: Hàm kiểm tra số Armstrong (Narcissistic numbers)

def cubesum(n):
    """Tính tổng các lập phương của các chữ số trong n"""
    n = abs(n)
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    
    return total

def isArmstrong(n):
    """Kiểm tra xem n có phải số Armstrong (cubesum(n) == n)"""
    return cubesum(n) == n

# Tìm tất cả số Armstrong (trong phạm vi hợp lý)
armstrong_numbers = []

print("Tìm kiếm số Armstrong...")
print("=" * 50)

# Kiểm tra từ 1 đến 10000
for n in range(1, 10001):
    if isArmstrong(n):
        armstrong_numbers.append(n)

print(f"Số Armstrong tìm thấy (1 - 10000):")
print(armstrong_numbers)

print(f"\nTất cả đều là số Armstrong vì cubesum(n) == n:")
print("-" * 50)
for num in armstrong_numbers:
    print(f"{num}: {' + '.join([d + '³' for d in str(num)])} = {cubesum(num)}")

# Kiểm tra số từ người dùng
print("\n" + "=" * 50)
try:
    num = int(input("Nhập một số để kiểm tra: "))
    cs = cubesum(num)
    
    if isArmstrong(num):
        print(f"✓ {num} là số Armstrong!")
        print(f"  cubesum({num}) = {cs} = {num}")
    else:
        print(f"✗ {num} không phải số Armstrong")
        print(f"  cubesum({num}) = {cs} ≠ {num}")
        
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
