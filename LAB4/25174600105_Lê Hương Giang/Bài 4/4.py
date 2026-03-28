n = int(input("Nhập số n: "))
S = 0
dem = 0

if n!=0:
    max = 0

while n!=0:
    S += n
    dem += 1

    if n > max :
        max = n

    n = int(input("Nhập số n: "))
print("Tổng = ",S)
print("Số lượng = ",dem)
print("Số lớn nhất = ",max)