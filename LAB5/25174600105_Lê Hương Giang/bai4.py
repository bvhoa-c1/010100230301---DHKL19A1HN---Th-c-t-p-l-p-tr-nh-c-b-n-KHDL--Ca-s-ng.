#a,
def so_nguyen_duong():
    while True:
        n = int(input("Nhập số nguyên dương"))
        if n > 0 :
            break
        print("n phải là số nguyên tố")
    return n
def P(n):
    s = 1 
    for i in range(1, n+1):
        s = s * 2*i + 1
    return s
n = so_nguyen_duong()
print(f"Tổng P(n) = 1x3x5...x(2n+1), với (n>0) là {P(n)}")
#b,
def S(n):
    s = 0
    for i in range(n+1):
        s += (-1)**(i+1) * i
    return s
n = int(input("Nhập số n: "))
if n > 0:
    print(f"S({n}) = {S(n)}")
else:
    print("n phải lớn hơn 0")
#c,
def S2(n):
    kq = 0
    s = 0
    for i in range(1,n+1):
        s += 1
        kq += s 
    return kq
n = int(input("Nhập số n: "))
if n > 0:
    print(f"S2({n})={S2(n)}")
else:
    print("n phải lớn hơn hoặc bằng 0")
#d,
def P2(x,y):
    return x**y
x = float(input("Nhập số x: "))
y = int(input("Nhập số y: "))
print(f"P2({x}, {y}) = {P2(x, y)}")
