def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

n = int(input("Nhập số lượng phần tử trong mảng: "))
arr = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(num)

result = []

for num in arr:
    if is_prime(num) or is_perfect(num):
        result.append(num)

print(f"\nMảng gốc: {arr}")
print(f"Các phần tử là số nguyên tố hoặc số hoàn hảo: {result}")

for num in result:
    prime_str = "số nguyên tố" if is_prime(num) else ""
    perfect_str = "số hoàn hảo" if is_perfect(num) else ""
    
    if is_prime(num) and is_perfect(num):
        print(f"{num} là số nguyên tố và số hoàn hảo")
    elif is_prime(num):
        print(f"{num} là {prime_str}")
    else:
        print(f"{num} là {perfect_str}")
