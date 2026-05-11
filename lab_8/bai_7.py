def sumPdivisors(n):
    if n <= 1:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total

a = int(input("a = "))
b = int(input("b = "))

print(a != b and sumPdivisors(a) == b and sumPdivisors(b) == a)
