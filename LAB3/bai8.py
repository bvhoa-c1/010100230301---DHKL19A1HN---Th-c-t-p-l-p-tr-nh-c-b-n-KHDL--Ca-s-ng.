def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

n = int(input("Nhap n: "))
max_num = max(range(1, n+1), key=sum_digits)
print(f"So co tong chu so lon nhat tu 1 den {n}: {max_num} (tong={sum_digits(max_num)})")
