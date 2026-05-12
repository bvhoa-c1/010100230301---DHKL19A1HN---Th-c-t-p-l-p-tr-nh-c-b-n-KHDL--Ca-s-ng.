#Bài8.1:
import math
def n_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("Các cặp số nguyên tố sinh đôi < 1000:")

for i in range(2, 1000):
    if n_to(i) and n_to(i + 2):
        print((i, i + 2))

#Bài8.2:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Nhập n: "))

print("Giai thừa =", factorial(n))

#Bài8.3:
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

def hoan_vi(n, r):
    return factorial(n) // factorial(n - r)

def to_hop(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Nhập n: "))
r = int(input("Nhập r: "))

print("Hoán vị =", hoan_vi(n, r))
print("Tổ hợp =", to_hop(n, r))

#Bài8.4:
def cubesum(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** 3
        n //= 10
    return total

n = int(input("Nhập n: "))

print("Tổng lập phương các chữ số =", cubesum(n))

#Bài8.5:
def cubesum(n):
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    return total

def isArmstrong(n):
    return cubesum(n) == n

print("Các số Armstrong < 1000:")

for i in range(1, 1000):
    if isArmstrong(i):
        print(i)

#Bài8.6:
def sumPdivisors(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total

n = int(input("Nhập n: "))

print("Tổng ước thực sự =", sumPdivisors(n))

#Bài8.7:
def sumPdivisors(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total
n = int(input("Nhập n: "))

def isAmicable(a, b):
    return (sumPdivisors(a) == b and sumPdivisors(b) == a)

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if isAmicable(a, b):
    print("Là cặp số Amicable")
else:
    print("Không phải")

#Bài8.8:
a = [1, 2, 3, 4, 5, 6, 7, 8]
chan = list(filter(lambda x: x % 2 == 0, a))
le = list(filter(lambda x: x % 2 != 0, a))
print("Số chẵn:", chan)
print("Số lẻ:", le)

#Bài8.9:
a = [1, 2, 3, 4, 5]
n = list(map(lambda x: x ** 3, a))
print(n)

#Bài8.10:
a = [1, 2, 3, 4, 5, 6]
lap_phuong = list(
    map(lambda x: x ** 3,
        filter(lambda x: x % 2 == 0, a)))
binh_phuong = list(
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 != 0, a)))
print("Chẵn lập phương:", lap_phuong)
print("Lẻ bình phuong:", binh_phuong)
