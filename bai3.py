#cau a
def nhap_n():
    return int(input("Nhập n: "))

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def bai3a():
    n = nhap_n()
    if la_so_nguyen_to(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải số nguyên tố")
#cau b
def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
def bai3b():
    n = nhap_n()
    if la_so_hoan_hao(n):
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải số hoàn hảo")

#cau c
def la_so_doi_xung(n):
    return str(n) == str(n)[::-1]

def bai3c():
    dem = 0
    for i in range(1, 1001):
        if la_so_doi_xung(i):
            print(f"{i:5}", end=" ")
            dem += 1
            
            if dem % 15 == 0:
                print()
