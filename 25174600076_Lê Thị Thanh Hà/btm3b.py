

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