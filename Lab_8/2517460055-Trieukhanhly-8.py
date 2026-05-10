#8.1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(2, 1000):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)
#8.2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input("Nhập n: "))
print(factorial(n))
#8.3
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def permutation(n, r):
    return factorial(n) // factorial(n - r)
def combination(n, r):
    return factorial(n) // (
        factorial(r) * factorial(n - r)
    )
print("Hoán vị:", permutation(5, 2))
print("Tổ hợp:", combination(5, 2))
#8.4
def cubesum(n):
    total = 0
    for digit in str(n):
        total += int(digit) ** 3
    return total
print(cubesum(123))
#8.5
def cubesum(n):
    total = 0
    for digit in str(n):
        total += int(digit) ** 3
    return total
def isArmstrong(n):
    return cubesum(n) == n
for i in range(1000):
    if isArmstrong(i):
        print(i)
#8.6
def sumPdivisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
print(sumPdivisors(6))
#8.7
def sumPdivisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total
def amicable(a, b):
    return (
        sumPdivisors(a) == b
        and
        sumPdivisors(b) == a
    )
print(amicable(220, 284))
#8.8
a = [1, 2, 3, 4, 5, 6]
even = list(
    filter(lambda x: x % 2 == 0, a)
)
odd = list(
    filter(lambda x: x % 2 != 0, a)
)
print(even)
print(odd)
#8.9
a = [1, 2, 3, 4]
cube = list(
    map(lambda x: x**3, a)
)
print(cube)
#8.10
a = [1, 2, 3, 4, 5]
result = list(
    map(
        lambda x:
            x**3 if x % 2 == 0
            else x**2,
        a
    )
)
print(result)