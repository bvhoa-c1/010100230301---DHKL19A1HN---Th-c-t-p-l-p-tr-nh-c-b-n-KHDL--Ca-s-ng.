n = int(input("Nhập n (>10): "))
a = 1
s1 = s2 = s3 = s4 = 0

while a <= n:
    # a) Tổng lũy thừa của 6
    s1 += 6**a
    
    # b) Tổng nghịch đảo lũy thừa (với mẫu số tăng 2 đơn vị mỗi bước)
    s2 += 1 / (3**(2*a - 1))
    
    # c) Tổng bình phương đan dấu
    s3 += ((-1)**a) * (a**2)
    
    # d) Tổng tích ba số liên tiếp
    s4 += a * (a + 1) * (a + 2)
    
    a += 1

print(f"S1: {s1}\nS2: {s2:.5f}\nS3: {s3}\nS4: {s4}")