n = int(input("Nhập số: "))
temp = n
tong = 0
tich = 0
dao = 0
while temp > 0:
    digit = temp % 10
    tong += digit 
    tich *= digit
    dao = dao *10 + digit
    temp //= 10
print("Tổng", tong)
print("Tích", tich)
print("Đảo", dao)