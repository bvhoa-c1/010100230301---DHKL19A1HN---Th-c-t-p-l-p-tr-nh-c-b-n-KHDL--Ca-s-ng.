n = int(input("Nhập n: "))

temp = n
tong = 0
tich = 1
dao = 0

# Trường hợp n = 0
if n == 0:
    tong = 0
    tich = 0
    dao = 0
else:
    while temp > 0:
        digit = temp % 10
        
        tong += digit
        tich *= digit
        dao = dao * 10 + digit
        
        temp //= 10

print("Tổng chữ số:", tong)
print("Tích chữ số:", tich)
print("Số đảo:", dao)