
while True:
    n = int(input("Nhập n (số nguyên dương): "))
    if n > 0:
        break
    print("Vui lòng nhập số lớn hơn 0!")

s1 = 0

for i in range(1, n + 1):
    s1 += 1 / i

print(f"Tổng nghịch đảo S1 của {n} số đầu tiên là: {s1:.4f}")