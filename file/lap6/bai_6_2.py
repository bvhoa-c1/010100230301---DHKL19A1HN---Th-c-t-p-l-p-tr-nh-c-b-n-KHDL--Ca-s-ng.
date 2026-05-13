# Bài 6.2: Trích xuất số nguyên tố và số hoàn hảo

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

n = int(input("Nhập số phần tử của mảng: "))
arr = []

print("Nhập các số nguyên dương:")
for i in range(n):
    num = int(input(f"Phần tử {i+1}: "))
    arr.append(num)

prime_numbers = []
perfect_numbers = []

for num in arr:
    if is_prime(num):
        prime_numbers.append(num)
    if is_perfect(num):
        perfect_numbers.append(num)

print(f"\nMảng nhập vào: {arr}")
print(f"Số nguyên tố: {prime_numbers}")
print(f"Số hoàn hảo: {perfect_numbers}")
