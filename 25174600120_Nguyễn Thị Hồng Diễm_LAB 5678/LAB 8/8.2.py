def giai_thua(n):
    gt = 1
    for i in range(1, n+1):
        gt*=1
    return gt
n = int(input("Nhập n:"))
print("Giai thừa bằng", giai_thua(n))