# Bài 8.7: Kiểm tra số Amicable (số bạn)

def sumPdivisors(n):
    """Tính tổng tất cả các ước số thực sự của n"""
    if n <= 1:
        return 0
    
    divisors_sum = 1
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    
    return divisors_sum

def is_amicable(a, b):
    """Kiểm tra xem a và b có phải cặp số Amicable"""
    return sumPdivisors(a) == b and sumPdivisors(b) == a

# Tìm tất cả cặp số Amicable < 10000
print("Tìm kiếm cặp số Amicable (Số bạn)")
print("=" * 60)

amicable_pairs = []

for a in range(1, 10000):
    b = sumPdivisors(a)
    if b > a and is_amicable(a, b):
        amicable_pairs.append((a, b))

print(f"Cặp số Amicable tìm thấy (< 10000):")
print("-" * 60)

for a, b in amicable_pairs:
    sum_a = sumPdivisors(a)
    sum_b = sumPdivisors(b)
    print(f"({a}, {b})")
    print(f"  sumPdivisors({a}) = {sum_a}")
    print(f"  sumPdivisors({b}) = {sum_b}")
    print()

print(f"Tổng cộng: {len(amicable_pairs)} cặp số Amicable")

# Kiểm tra cặp số từ người dùng
print("\n" + "=" * 60)
try:
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    
    sum_a = sumPdivisors(a)
    sum_b = sumPdivisors(b)
    
    print(f"\nsumPdivisors({a}) = {sum_a}")
    print(f"sumPdivisors({b}) = {sum_b}")
    
    if is_amicable(a, b):
        print(f"✓ ({a}, {b}) là cặp số Amicable!")
    else:
        print(f"✗ ({a}, {b}) không phải cặp số Amicable")
        
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ!")
