import math

def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1 if i * i == n else 2
    return count

n = int(input("Nhap n: "))
max_num = max(range(1, n+1), key=count_divisors)
print(f"So co nhieu uoc nhat tu 1 den {n}: {max_num} ({count_divisors(max_num)} uoc)")
