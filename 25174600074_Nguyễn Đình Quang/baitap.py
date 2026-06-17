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

# Bài 3
# A
def kt_nguyento():
    if n <= 1:
        return False
    for i in range(2, n):
        return False
    return True
def nhap_so_nguyenduong():
    while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        print("n là số ngn=uyên dương")
    return n
n = nhap_so_nguyenduong()
if kt_nguyento():
    print("n là số nguyên tố")
else:
    print("n không phải là số nguyên tố")
# B
def kt_so_hoan_hao(n):
    if n <= 1:
        return False
    tong_cac_uoc = 1
    for i in range(2, int(n ** 0,5) + 1):
        if n % i == 0:
            tong_cac_uoc += i
            if i != n // i:
                tong_cac_uoc += n // i
    return tong_cac_uoc == n
def nhap_so_nguyenduong():
    while True:
        n = int(input('Nhập số nguyên dương n :'))
        if n > 0:
            break
        print(" n là số nguyên dương")
    return n
n = nhap_so_nguyenduong()
if kt_so_hoan_hao(n):
    print(" n là số hoàn hảo")
else:
    print("n không phải số hoàn hảo")
# C
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print("Các số đối xứng trong phạm vui 1000 là: ")
count = 0
for i  in range( 1, 1000):
    if is_palindrome(i):
        print(str(i).rjust(3), end="")
        count += 1
        if count % 15 == 0:
            print("")


# Bài 4
# A
def calculate_P(n):
    result = 1
    for i in range(1, n + 1):
        result *= 2 * i + 1
    return result
def nhap_so_nguyenduong():
    while True:
        n = int(input("Nhập số nguyên dương n:"))
        if n > 0:
            break
        print("n là số nguyên dương")
    return n
n = nhap_so_nguyenduong()
print("tổng P(n)=1x3x5...x(2n+1), với (n >=0) là", calculate_P(n))
# B
def tinh_tong(n):
    kq = 0
    for i in range(n + 1):
        kq += (-1)**(i+1) * i
    return kq
n = int(input("Nhập n: "))
if n >= 0:
    print("S({}) = {}".format(n,tinh_tong(n)))
else:
    print("n phải >= 0")
# C
def tinh_tong_S(n):
    kq = 0
    sum = 0
    for i in range(1,n+1):
        sum += i
        kq += sum
    return kq
n = int(input("Nhập n: "))
if n >= 0:
    print("S({}) = {}".format(n,tinh_tong_S(n)))
else:
    print("n phải >= 0")
# D
def luy_thua(x, y):
    return x ** y
if __name__=="__main__":
    x = float(input("Nhập x: "))
    y = int(input('Nhập y: '))
    print("P({}, {}) = {}".format(x,y,luy_thua(x,y)))

# Bài 5
import msvcrt
def XemAscii():
    print("Nhấn phím bất kì để xem giá trị ASCII, nhấn ESC để kết thúc ")