n = int(input("Nhập n: "))
max_div = 1
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        max_div = max(max_div, i)
        if i != n // i and n // i != n:
            max_div = max(max_div, n // i)
print(max_div)
