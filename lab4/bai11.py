n = int(input("Nhập n (n > 10): "))
while n <= 10:
    n = int(input("Vui lòng nhập n lớn hơn 10: "))

a = 1
s1, s2, s3, s4 = 0, 0, 0, 0

while a <= n:
    # a) S1 = 6 + 6^2 + ... + 6^a
    s1 += 6**a
    
    # b) S2 = 1/3 + 1/3^3 + ... + 1/3^(2a+1)
    s2 += 1 / (3**(2*a - 1)) # Sửa lại quy luật theo hình: 3^1, 3^3, 3^5...
    
    # c) S3 = -1^2 + 2^2 - 3^2 + ... + (-1)^a * a^2
    s3 += ((-1)**a) * (a**2)
    
    # d) S4 = 1.2.3 + 2.3.4 + ... + a.(a+1).(a+2)
    s4 += a * (a + 1) * (a + 2)
    
    a += 1

print(f"S1 = {s1}")
print(f"S2 = {s2:.4f}")
print(f"S3 = {s3}")
print(f"S4 = {s4}")