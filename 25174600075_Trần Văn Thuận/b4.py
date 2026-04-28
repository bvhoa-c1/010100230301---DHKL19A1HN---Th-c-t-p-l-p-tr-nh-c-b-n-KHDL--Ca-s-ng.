# a,
def tinh_tich_le(n):
    p = 1
    for i in range(1, 2*n + 2, 2):
        p *= i
    return p

n = int(input("Nhập n (n >= 0): "))
print(f"P({n}) = {tinh_tich_le(n)}")
# b,
def tinh_tong_dan_dau(n):
    s = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            s += i
        else:
            s -= i
    return s

n = int(input("Nhập n (n >= 0): "))
print(f"S({n}) = {tinh_tong_dan_dau(n)}")

# c,
def tinh_tong_kep(n):
    tong_lon = 0
    tong_con = 0
    for i in range(1, n + 1):
        tong_con += i      
        tong_lon += tong_con
    return tong_lon

n = int(input("Nhập n: "))
print(f"S({n}) = {tinh_tong_kep(n)}")

# d,
def tinh_luy_thua(x, y):
    return x ** y

x = float(input("Nhập cơ số x: "))
y = float(input("Nhập số mũ y: "))
print(f"P({x}, {y}) = {tinh_luy_thua(x, y)}")