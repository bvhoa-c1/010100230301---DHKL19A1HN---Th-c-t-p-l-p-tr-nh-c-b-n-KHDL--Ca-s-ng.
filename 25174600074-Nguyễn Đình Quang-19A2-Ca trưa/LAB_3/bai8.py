n = int(input("Nhập n: "))
max_num = 1
max_sum = 0

for i in range(1, n+1):
    s = sum(int(d) for d in str(i))
    if s > max_sum:
        max_sum = s
        max_num = i

print("Số cần tìm:", max_num)