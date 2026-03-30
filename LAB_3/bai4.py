import math

# 1. Nhập n và kiểm tra điều kiện (n > 0)
while True:
    try:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            break
        else:
            print("Vui lòng nhập n lớn hơn 0!")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

# Khởi tạo các giá trị tổng ban đầu
s1 = 0
s2 = 0
s3 = 0
s4 = 0

# 2. Tính toán các tổng bằng vòng lặp
for i in range(1, n + 1):
    # a) S1 = 1 + 2 + ... + n
    s1 += i
    
    # b) S2 = 1/1 + 1/2 + ... + 1/n
    s2 += 1 / i
    
    # c) S3 = 1/√2 + 1/√4 + ... + 1/√2n
    s3 += 1 / math.sqrt(2 * i)
    
    # d) S4 = 1/1 - 1/2 + 1/3 - ... + (-1)^(n+1)/n
    s4 += ((-1)**(i + 1)) / i

# 3. In kết quả (làm tròn 4 chữ số thập phân cho các phân số)
print("-" * 30)
print(f"S1 = {s1}")
print(f"S2 = {s2:.4f}")
print(f"S3 = {s3:.4f}")
print(f"S4 = {s4:.4f}")