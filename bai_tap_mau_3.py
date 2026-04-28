# a: Kiểm tra số nguyên tố
def nhap_so():
    n = int(input("Nhập số nguyên dương n: "))
    return n

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = nhap_so()

if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")


# b: Kiểm tra số hoàn hảo
def nhap_so():
    n = int(input("Nhập số nguyên dương n: "))
    return n

def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

n = nhap_so()

if la_so_hoan_hao(n):
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải là số hoàn hảo")


# c: In các số đối xứng trong phạm vi 1000
def la_so_doi_xung(n):
    return str(n) == str(n)[::-1]

dem = 0

for i in range(1, 1001):
    if la_so_doi_xung(i):
        print(f"{i:5}", end="")
        dem += 1
        
        if dem % 15 == 0:
            print()