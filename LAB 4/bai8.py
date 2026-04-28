n = int(input("Nhap n:"))

a = n
tong = 0
tich = 1
dao = 0

while a > 0:
    b = a % 10
    tong += b
    tich *= b
    dao = dao * 10 + b
    a = a // 10
print("Tong chu so la :",tong)
print("Tich chu so la :",tich)
print("So dao la :",dao)