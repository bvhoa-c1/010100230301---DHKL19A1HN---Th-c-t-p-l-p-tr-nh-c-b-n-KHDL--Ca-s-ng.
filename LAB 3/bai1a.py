tong = 0 
for i in range(2000,4000):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print(tong)