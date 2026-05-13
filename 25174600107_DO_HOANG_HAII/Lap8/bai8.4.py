def cubesum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    return total

num = int(input("Nhập một số nguyên dương: "))

result = cubesum(num)
print(f"Tổng các lập phương của chữ số: {result}")
