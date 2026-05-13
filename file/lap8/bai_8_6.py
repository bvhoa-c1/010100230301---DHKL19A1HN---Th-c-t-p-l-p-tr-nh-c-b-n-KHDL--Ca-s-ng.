# Bài 8.6: Hàm sumPdivisors - tính tổng các ước số thực sự

def sumPdivisors(n):
    """Tính tổng tất cả các ước số thực sự của n (không tính n)"""
    if n <= 1:
        return 0
    
    divisors_sum = 1  # 1 luôn là ước số
    
    # Chỉ cần kiểm tra đến căn bậc 2 của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            # Nếu i không phải căn bậc 2 của n, thêm n/i
            if i != n // i:
                divisors_sum += n // i
    
    return divisors_sum

def get_divisors(n):
    """Lấy danh sách tất cả các ước số thực sự của n"""
    if n <= 1:
        return []
    
    divisors = [1]
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    return sorted(divisors)

# Kiểm tra hàm
print("Ước số thực sự của các số")
print("=" * 60)
print(f"{'n':<5} {'Ước số thực sự':<35} {'Tổng':<10}")
print("-" * 60)

test_numbers = [6, 12, 28, 100, 120, 220, 284]

for num in test_numbers:
    divisors = get_divisors(num)
    total = sumPdivisors(num)
    divisors_str = " + ".join(map(str, divisors))
    print(f"{num:<5} {divisors_str:<35} {total:<10}")

# Nhập từ người dùng
print("\n" + "=" * 60)
try:
    num = int(input("Nhập một số nguyên dương: "))
    
    if num > 1:
        divisors = get_divisors(num)
        total = sumPdivisors(num)
        
        print(f"\nƯớc số thực sự của {num}: {divisors}")
        print(f"Tổng ước số thực sự: {total}")
    else:
        print("Vui lòng nhập số > 1")
        
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
