n = int(input("Nhập n: "))
count = 0

for i in range(1, n+1):
    tong = sum(int(d) for d in str(i))
    if tong % 2 == 0:
        count += 1

print("Số lượng:", count)