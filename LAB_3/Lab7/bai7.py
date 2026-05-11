n = int(input("Nhập n: "))
count = 0
for i in range(1, n + 1):
    s = 0
    temp = i
    while temp > 0:
        s += temp % 10
        temp //= 10
    if s % 2 == 0:
        count += 1
print("Số lượng:", count)