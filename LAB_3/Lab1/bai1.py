tong1 = 0
tong2 = 0
#cau a
for i in range(2000, 4001):
    if i % 7 == 0 and i % 5 != 0:
        tong1 += i
#cau b 
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong2 += i
print("Tổng câu a là:", tong1)
print("Tổng câu b là:", tong2)