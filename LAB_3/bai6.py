# Bài 6: Tính tổng nghịch đảo của n số nguyên đầu tiên S1 = 1 + 1/2 + ... + 1/n

n = int(input("Nhập n: "))
s1 = 0.0
for i in range(1, n+1):
    s1 += 1 / i

print(f"S1 = {s1}")
