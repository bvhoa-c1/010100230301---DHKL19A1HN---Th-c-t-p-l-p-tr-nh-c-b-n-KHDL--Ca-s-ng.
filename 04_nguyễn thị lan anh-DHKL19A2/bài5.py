n = int(input("Nhap n: "))

temp = n
dao = 0

while temp > 0:
    du = temp % 10
    dao = dao * 10 + du
    temp //= 10

if dao == n:
    print("So doi xung")
else:
    print("Khong doi xung")
    