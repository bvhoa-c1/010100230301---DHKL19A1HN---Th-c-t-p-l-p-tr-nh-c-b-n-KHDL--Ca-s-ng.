n = int(input("Nhap n: "))
temp = n
dao = 0

while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10

if dao == n:
    print("Dung")
else:
    print("Sai")