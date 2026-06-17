n = int(input("Nhap n: "))

temp = n
tong = 0

while temp > 0:
    du = temp % 10
    tong += du ** 3
    temp //= 10

if tong == n:
    print("So Armstrong")
else:
    print("Khong phai Armstrong")