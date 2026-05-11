import math

def isPrime(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:
            return False

    return True

s = input("Nhap chuoi: ")

digits = ""

for c in s:

    if c.isdigit():
        digits += c

if digits == "":
    print("Khong co chu so")
else:
    num = int(digits)

    print("So sau khi loc:", num)

    if isPrime(num):
        print("La so nguyen to")
    else:
        print("Khong phai so nguyen to")