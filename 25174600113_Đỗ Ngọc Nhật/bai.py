# Bài 1
def luythua():
    x = int(input("Nhập số x = "))
    n = int(input("Nhập số mũ n = "))
    print("Lũy thừa của",x,"mũ",n,"=", x**n)
    return()
luythua()
# Bài 2
def in_fibonacci(n):
    fib1 = 0
    fib2 = 1
    i = 0
    while i < n:
        print(fib1, end="")
        fib_sum = fib1 + fib2
        fib2 = fib_sum
        i += 1
print(" 10 số fibonacci đầu tiên :")
in_fibonacci(10)
# Bài 3:
# a
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập n: "))
if is_prime(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")
# b
def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n
n = int(input("Nhập n: "))
if is_perfect(n):
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải số hoàn hảo")
# c
def is_palindrome(n):
    return str(n) == str(n)[::-1]
count = 0  
for i in range(1, 1001):
    if is_palindrome(i):
        print(f"{i:05}", end=" ")
        count += 1
        if count == 15:  
            print()
            count = 0
# Bài 4:
#a
def P(n):
    result = 1
    for i in range(n + 1):
        result *= (2*i + 1)
    return result
n = int(input("Nhập n: "))
print("P(n) =", P(n))
#b
def S(n):
    s = 0
    for i in range(1, n + 1):
        s += (-1)**(i+1) * i
    return s
n = int(input("Nhập n: "))
print("S(n) =", S(n))
#c
def S2(n):
    total = 0
    for i in range(1, n + 1):
        total += sum(range(1, i + 1))
    return total
n = int(input("Nhập n: "))
print("S(n) =", S2(n))
#d
def power(x, y):
    return x ** y
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print("P(x,y) =", power(x, y))
# Bài 5:
def ascii_value():
    while True:
        ch = input("Nhập ký tự (gõ ESC để thoát): ")

        if ch == "ESC":
            print("Thoát chương trình")
            break

        if len(ch) == 1:
            print("ASCII:", ord(ch))
        else:
            print("Chỉ nhập 1 ký tự!")
ascii_value()