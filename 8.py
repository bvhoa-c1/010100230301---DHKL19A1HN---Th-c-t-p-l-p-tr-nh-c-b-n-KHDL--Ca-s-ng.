n = int(input())
a = n
dao = 0
tong = 0
tich = 1
while n != 0:
    cac_so = n % 10
    print(cac_so , end=(" "))
    tich *= cac_so
    tong += cac_so
    n //= 10
while a != 0:
    dao = dao * 10 + a % 10
    a //= 10

print("\ntích các số ", tich)
print("tong cac so", tong)
print("so dao " , dao)


