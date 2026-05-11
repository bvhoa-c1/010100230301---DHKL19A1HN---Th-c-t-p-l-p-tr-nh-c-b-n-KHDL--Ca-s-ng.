

def tinh_S_c(n):
    s = 0
    tong_phu = 0
    for i in range(1, n + 1):
        tong_phu += i
        s += tong_phu
    return s

n = int(input("Nhập n: "))
print("S(n) =", tinh_S_c(n))