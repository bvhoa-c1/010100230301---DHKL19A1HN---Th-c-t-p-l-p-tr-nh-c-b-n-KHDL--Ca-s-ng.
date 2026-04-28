# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Khởi tạo các biến
tong = 0
tich = 1
so_dao = 0
temp = n

print("Các chữ số được tách ra là:", end=" ")

# Vòng lặp tách từng chữ số từ phải sang trái
while temp > 0:
    chu_so = temp % 10          # Lấy chữ số cuối cùng
    print(chu_so, end=" ")     
    
    tong += chu_so              
    tich *= chu_so             
    so_dao = so_dao * 10 + chu_so # Xây dựng số đảo
    
    temp //= 10                 # Bỏ chữ số cuối cùng đã xử lý

# Hiển thị kết quả
print(f"\n{'-'*20}")
print(f"Tổng các chữ số: {tong}")
print(f"Tích các chữ số: {tich}")
print(f"Số đảo ngược của {n} là: {so_dao}")