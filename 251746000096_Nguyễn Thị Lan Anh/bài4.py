# a) Tính P(n) = 1 * 3 * 5 * ... * (2n+1)

def cau_a():
    n = int(input("Nhập n: "))
    p = 1
    
    for i in range(n + 1):
        p *= (2 * i + 1)
    
    print("P(n) =", p)


# b) Tính S(n) = 1 - 2 + 3 - 4 + ... + (-1)^(n+1) * n

def cau_b():
    n = int(input("Nhập n: "))
    s = 0
    
    for i in range(1, n + 1):
        s += (-1) ** (i + 1) * i
    
    print("S(n) =", s)


# c) Tính S(n)=1+(1+2)+(1+2+3)+...+(1+2+...+n)

def cau_c():
    n = int(input("Nhập n: "))
    s = 0
    
    for i in range(1, n + 1):
        tong = 0
        for j in range(1, i + 1):
            tong += j
        s += tong
    
    print("S(n) =", s)


# d) Tính P(x,y) = x^y

def cau_d():
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    
    p = x ** y
    
    print("P(x,y) =", p)


# Gọi hàm
cau_a()
cau_b()
cau_c()
cau_d()