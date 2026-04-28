n = int(input("Nhập n: "))

temp = n
dem = 0

while temp > 0:
    dem += 1
    temp = temp // 10

temp = n
tong = 0

while temp > 0:
    digit = temp % 10      
    tong += digit ** dem  
    temp = temp // 10            

if tong == n:
    print(n, "là số Armstrong")
else:
    print(n, "không phải số Armstrong")