# 1. Nhập n và kiểm tra điều kiện n > 10
while True:
    try:
        n = int(input("Nhập số nguyên n (n > 10): "))
        if n > 10:
            break
        else:
            print("Vui lòng nhập n lớn hơn 10!")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

# Khởi tạo các biến tổng
s1 = 0
s2 = 0
s3 = 0
s4 = 0

# Biến đếm a bắt đầu từ 1
a = 1

# 2. Vòng lặp while - Chương trình dừng khi a vượt quá n
while a <= n:
    # a) S1 = 6 + 6^2 + ... + 6^a
    s1 += 6**a
    
    # b) S2 = 1/3^1 + 1/3^3 + ... + 1/3^(2a-1)
    # Lưu ý quy luật mẫu số là các số lẻ: 1, 3, 5... ứng với (2*a - 1)
    s2 += 1 / (3**(2 * a - 1))
    
    # c) S3 = -1^2 + 2^2 - 3^2 + ... + (-1)^a * a^2
    s3 += ((-1)**a) * (a**2)
    
    # d) S4 = 1.2.3 + 2.3.4 + ... + a.(a+1).(a+2)
    s4 += a * (a + 1) * (a + 2)
    
    # Quan trọng: Tăng biến đếm a để không bị lặp vô hạn
    a += 1

# 3. In kết quả
print("-" * 30)
print(f"S1 = {s1}")
print(f"S2 = {s2:.10f}") # S2 thường rất nhỏ nên in nhiều chữ số thập phân
print(f"S3 = {s3}")
print(f"S4 = {s4}")