n = 0
while n <= 0:
    n = int(input("Nhập n nguyên dương: "))
# c) S3 = 1/√2 + 1/√4 + ... + 1/√(2n)
import math
s3 = sum(1/math.sqrt(2*i) for i in range(1, n + 1))
print(s3)