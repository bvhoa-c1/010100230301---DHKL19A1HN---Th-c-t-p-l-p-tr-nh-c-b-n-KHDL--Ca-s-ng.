#a
def tinh_p():
    n = int(input("Nhập n(n >= 0): "))
    p = 1
    for i in range(1, (2*n+1) +1, 2):
        p *= i
    print(f"kq p({n}) = {p}")
tinh_p()

#b
def tinh_s():
    n = int(input("Nhập n (n>=0): "))
    s = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            s += i
        else:
            s -= i
    print(f"kq s{n}={s}")
tinh_s()

#c
def tinh_S():
    n = int(input("Nhập n (n >= 1): "))
    s = 0
    tong = 0
    for i in range(1, n+1):
        tong += i
        s += tong
    print(f"kq s{n} = {s}")
tinh_S()

#d
def tinh_P():
    x = float(input("Nhập cơ số x: "))
    y = int(input("Nhập số mũ y(y > = 0): "))
    p = 1
    for _ in range(y):
        p *= x
    print(f"Kq {x} ^ {y} = {p}")
tinh_P()