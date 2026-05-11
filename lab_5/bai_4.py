import math

s = input("s = ")
digits = "".join(ch for ch in s if ch.isdigit())

if digits == "":
    print("No digits")
else:
    n = int(digits)
    prime = n >= 2
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            prime = False
            break
    print(n)
    print(prime)
