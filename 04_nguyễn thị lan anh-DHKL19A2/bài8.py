n = int(input("Nhap n: "))

tong = 0
tich = 1
dao = 0

while n > 0:
    du = n % 10

    tong += du
    tich *= du
    dao = dao * 10 + du

    n //= 10

print("Tong =", tong)
print("Tich =", tich)
print("So dao =", dao)