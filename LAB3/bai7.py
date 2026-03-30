def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

n = int(input("Nhap n: "))
count = sum(1 for i in range(1, n+1) if sum_digits(i) % 2 == 0)
print(f"So luong so co tong chu so chan tu 1 den {n}: {count}")
