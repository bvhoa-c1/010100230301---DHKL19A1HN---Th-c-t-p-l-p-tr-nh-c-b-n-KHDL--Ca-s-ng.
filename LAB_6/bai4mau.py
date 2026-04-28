def P(n):
    result = 1
    for i in range(n + 1):
        result *= (2*i + 1)
    return result
def S(n):
    result = 0
    for i in range(1, n + 1):
        result += i if i % 2 == 1 else -i
    return result
def S2(n):
    result = 0
    temp = 0
    for i in range(1, n + 1):
        temp += i      # (1+2+...+i)
        result += temp
    return result
def Pxy(x, y):
    return x ** y
n = int(input("Nhập n: "))
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

print("P(n) =", P(n))
print("S(n) =", S(n))
print("S2(n) =", S2(n))
print("P(x, y) =", Pxy(x, y))