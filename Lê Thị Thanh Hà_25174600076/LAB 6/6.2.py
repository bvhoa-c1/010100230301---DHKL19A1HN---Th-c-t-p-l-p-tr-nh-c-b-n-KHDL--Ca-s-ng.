def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_perfect(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong == n


n = int(input("Nhập số lượng phần tử: "))

a = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(x)

result = []

for x in a:
    if is_prime(x) or is_perfect(x):
        result.append(x)

print("Các phần tử thỏa điều kiện:", result)
