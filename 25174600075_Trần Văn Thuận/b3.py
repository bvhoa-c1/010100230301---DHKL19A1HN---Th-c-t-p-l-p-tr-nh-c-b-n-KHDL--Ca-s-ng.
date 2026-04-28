# a,

import math

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Nhập số nguyên dương n: "))
if kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")

# b,
def kiem_tra_so_hoan_hao(n):
    if n <= 0: return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n
n = int(input("Nhập số nguyên dương n: "))
if kiem_tra_so_hoan_hao(n):
    print(f"{n} là số hoàn hảo.")
else:
    print(f"{n} không phải là số hoàn hảo.")


# c,
def la_so_doi_xung(n):
    s = str(n)
    return s == s[::-1]

def in_danh_sach_doi_xung():
    dem = 0
    print("Các số đối xứng trong phạm vi 1000:")
    for i in range(1001):
        if la_so_doi_xung(i):
            print(f"{i:5d}", end="")
            dem += 1
            
            if dem % 15 == 0:
                print()
    print() 

in_danh_sach_doi_xung()