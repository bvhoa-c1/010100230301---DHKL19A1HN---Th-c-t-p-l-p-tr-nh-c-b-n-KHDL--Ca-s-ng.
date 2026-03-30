#caua
tong = 0
for n in range(2000,4001):
    if n % 7 == 0 and n % 5 != 0:
        tong += n
print("tổng cuối cùng caua =  ", tong)
''
#caub
tong = 0
for n in range(500,1001):
    if n % 4 == 0 and n % 6 != 0:
        tong += n
print("tổng cuối cùng caub = ", tong)
