#8.1
def nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

for i in range(2, 1000):
    if nguyen_to(i) and nguyen_to(i + 2):
        print(i, i + 2)


#8.2
def giaithua(n):
    gt = 1

    for i in range(1, n + 1):
        gt *= i

    return gt

n = int(input("Nhập n: "))

print(giaithua(n))


#8.3
def giaithua(n):
    gt = 1

    for i in range(1, n + 1):
        gt *= i

    return gt

def hoanvi(n, r):
    return giaithua(n) // giaithua(n-r)

def tohop(n, r):
    return giaithua(n) // (giaithua(r) * giaithua(n-r))

n = int(input("n = "))
r = int(input("r = "))

print("Hoán vị =", hoanvi(n, r))
print("Tổ hợp =", tohop(n, r))



#8.4
def cubesum(n):
    tong = 0

    for i in str(n):
        tong += int(i) ** 3

    return tong

n = int(input("Nhập số: "))

print(cubesum(n))



#8.5
def cubesum(n):
    tong = 0

    for i in str(n):
        tong += int(i) ** 3

    return tong

def isArmstrong(n):
    return n == cubesum(n)

for i in range(1000):
    if isArmstrong(i):
        print(i)



#8.6
def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong

n = int(input("Nhập n: "))

print(sumPdivisors(n))



#8.7
def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong

def amicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a

a = int(input("a = "))
b = int(input("b = "))

if amicable(a, b):
    print("Là cặp Amicable")
else:
    print("Không phải")



#8.8
a = [1, 2, 3, 4, 5, 6]

chan = list(filter(lambda x: x % 2 == 0, a))
le = list(filter(lambda x: x % 2 != 0, a))

print("Chẵn:", chan)
print("Lẻ:", le)


#8.9
a = [1, 2, 3, 4]

b = list(map(lambda x: x**3, a))

print(b)


#8.10
a = [1, 2, 3, 4, 5, 6]

chan = list(map(lambda x: x**3,
                filter(lambda x: x % 2 == 0, a)))

le = list(map(lambda x: x**2,
             filter(lambda x: x % 2 != 0, a)))

print("Chẵn lập phương:", chan)
print("Lẻ bình phương:", le)