def giai_thua(n):
    gt = 1
    for i in range(1, n+1):
        gt *= i
    return gt
def hoan_vi(n, r):
    return giai_thua(n) // giai_thua(n-r)
def to_hop(n, r):
    return giai_thua(n) // (giai_thua(r) * giai_thua(n-r))
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
print("Hoán vị:", hoan_vi(n, r))
print("Tổ hợp:", to_hop(n, r))