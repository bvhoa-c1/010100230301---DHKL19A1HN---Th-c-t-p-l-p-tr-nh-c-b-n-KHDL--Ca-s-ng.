n = int(input("Nhập số n: "))
so = 0
S = 0

for i in range(1,n+1):
    tong = 0
    for j in range(1,i+1):
        if i%j==0:
            tong += 1
    if tong > S:
        S = tong
        so = i
print("Số có nhiều ước nhất là :",so)