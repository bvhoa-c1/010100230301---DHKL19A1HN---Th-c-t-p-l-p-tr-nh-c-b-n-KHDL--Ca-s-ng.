# ý a
tong_a  = 0
for i in range(2000, 4001):
    if i % 7 == 0 and  i % 5 != 0:
        tong_a += i
print("tổng câu a:",{tong_a})

# ý b
tong_b = 0
for i in range(500, 1001):
    if i % 4 == 0 and i % 6 != 0:
        tong_b += i
print("tổng câu b:",{tong_b})