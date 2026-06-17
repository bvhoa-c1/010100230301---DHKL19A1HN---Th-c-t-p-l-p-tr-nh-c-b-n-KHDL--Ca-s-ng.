#a
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN =", ucln(a, b))

#b
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return a * b // ucln(a, b)


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("BCNN =", bcnn(a, b))

#c
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

g = ucln(tu, mau)

tu //= g
mau //= g

print("Phân số rút gọn:", tu, "/", mau)