n = int(input("Nhap n:"))

while True:
    if n>0 :
        break
    else:
        print("Yeu cau nhap lai!")

Tong = 0
for i in range(1,n+1):
    Tong += (-1) ** n+1 / n
print("Tong = " ,Tong)