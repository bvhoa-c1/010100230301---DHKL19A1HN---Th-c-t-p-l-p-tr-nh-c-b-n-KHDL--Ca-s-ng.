n = int(input("Nhập n: "))
count = 0

for i in range(1, n + 1):
    s = 0
    for digit in str(i):
        s += int(digit)
    if s % 2 == 0:
        count += 1

print("Số lượng =", count)