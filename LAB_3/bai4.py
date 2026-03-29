import math

while True:
    n = int(input("Nhập n nguyên dương: "))
    if n > 0:
        break
    print("Vui lòng nhập lại!") [cite: 20]

# a) S1 = 1 + 2 + ... + n [cite: 22]
s1 = sum(range(1, n + 1))

# b) S2 = 1/1 + 1/2 + ... + 1/n [cite: 23, 28]
s2 = 0
for i in range(1, n + 1):
    s2 += 1/i

# c) S3 = 1/√2 + 1/√4 + ... + 1/√2n [cite: 24]
s3 = 0
for i in range(1, n + 1):
    s3 += 1 / math.sqrt(2 * i)

# d) S4 = 1/1 - 1/2 + ... [cite: 25]
s4 = 0
for i in range(1, n + 1):
    s4 += ((-1)**(i+1)) / i

print(f"S1: {s1}, S2: {s2:.2f}, S3: {s3:.2f}, S4: {s4:.2f}")