n = int(input("Nhap n: "))

tong = 0
tich = 1
dao = 0

temp = n

while temp > 0:
    digit = temp % 10
    
    tong += digit
    tich *= digit
    dao = dao * 10 + digit
    
    temp //= 10

print("Tong chu so =", tong)
print("Tich chu so =", tich)
print("So dao =", dao)