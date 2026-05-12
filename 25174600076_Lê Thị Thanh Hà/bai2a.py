def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("UCLN:", ucln(a, b))