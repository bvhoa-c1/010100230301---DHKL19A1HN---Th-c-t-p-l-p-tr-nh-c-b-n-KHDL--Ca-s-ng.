n = int(input(' nhập số nguyên dương:  ')) 
a = 0
b = 0
for i in range(1, n + 1):
    tong = 0
    for j in str(i):
        tong += int(j)
    if tong > a:
        a = tong
        b = i
print(b)