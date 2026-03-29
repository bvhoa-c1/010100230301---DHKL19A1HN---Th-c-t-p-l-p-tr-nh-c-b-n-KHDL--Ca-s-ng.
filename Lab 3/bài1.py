#a
tong = 0
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong += i
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 từ 2000 đến 4000 là:", tong)
#b
tong = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 từ 500 đến 1000 là:", tong)