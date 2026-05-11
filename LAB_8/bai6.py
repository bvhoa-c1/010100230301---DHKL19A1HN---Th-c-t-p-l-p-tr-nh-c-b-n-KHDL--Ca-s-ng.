def sumDivisors(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total

n = int(input("Nhap n: "))

print("Tong uoc so:", sumDivisors(n))