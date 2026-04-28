# cau a
def P_a(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2*i + 1)
    return tich
# cau b
def S_b(n):
    tong = 0
    for i in range(1, n+1):
        tong += (-1)**(i+1) * i
    return tong
#cau c
def S_c(n):
    tong = 0
    for i in range(1, n+1):
        tong += sum(range(1, i+1))
    return tong
#cau d
def P_d(x, y):
    ket_qua = 1
    for i in range(y):
        ket_qua *= x
    return ket_qua

print(P_a(3))
print(S_b(5))
print(S_c(4))
print(P_d(2, 3))
