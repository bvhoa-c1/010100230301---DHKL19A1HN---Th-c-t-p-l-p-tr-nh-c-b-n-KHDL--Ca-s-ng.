def la_so_ngto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def so_hoan_hao(n):
    if n < 2:
        return False
    tong = 0
    for i in range(1, n):
        if n %i == 0:
            tong += i
    return tong == n
n = int(input("nhập n: "))
a = []
for i in range(n):
    so = int(input(f"Nhập số thứ {i+1}: "))
    a.append(so)
kq = []
for x in a:
    if la_so_ngto(x) or so_hoan_hao(x):
        kq.append(x)
print("các số thỏa mãn là:", kq)