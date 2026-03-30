n = int(input("Nhập số n: "))
temp = n
tong = 0
tich = 1 
dao = 0
if n == 0: 
    tong = tich = dao = 0 
else: 
    while temp != 0: 
        chu_so = temp % 10 
        tong += chu_so
        tich += chu_so
        dao *= chu_so
        temp = temp // 10
print("Tổng chữ số là:", tong)
print("Tích chữ số là:", tich)
print("Số đảo là:", dao)