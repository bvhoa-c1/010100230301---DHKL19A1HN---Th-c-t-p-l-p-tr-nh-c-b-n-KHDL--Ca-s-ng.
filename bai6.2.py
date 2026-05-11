# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Kiểm tra số hoàn hảo
def is_perfect(n):
    if n < 2:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

arr = []

# Nhập mảng
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    arr.append(x)

result = []

# Tìm các số nguyên tố hoặc số hoàn hảo
for num in arr:

    if is_prime(num) or is_perfect(num):
        result.append(num)

# Hiển thị kết quả
print("Các phần tử thỏa điều kiện:")
print(result)