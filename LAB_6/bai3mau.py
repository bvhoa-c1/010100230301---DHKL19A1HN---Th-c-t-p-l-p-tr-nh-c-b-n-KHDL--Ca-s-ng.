#
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nhap_va_kiem_tra_snt():
    n = int(input("Nhập số nguyên dương n: "))
    if la_so_nguyen_to(n):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")
#  
def la_so_hoan_hao(n):
    if n <= 0:
        return False
    
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    
    return tong == n

def nhap_va_kiem_tra_hoan_hao():
    n = int(input("Nhập số nguyên dương n: "))
    if la_so_hoan_hao(n):
        print(f"{n} là số hoàn hảo")
    else:
        print(f"{n} không phải là số hoàn hảo")
#
def la_so_doi_xung(n):
    return str(n) == str(n)[::-1]

def in_so_doi_xung():
    dem = 0
    for i in range(1000):
        if la_so_doi_xung(i):
            print(f"{i:5}", end=" ")
            dem += 1
            
            if dem % 15 == 0:
                print()  # xuống dòng      