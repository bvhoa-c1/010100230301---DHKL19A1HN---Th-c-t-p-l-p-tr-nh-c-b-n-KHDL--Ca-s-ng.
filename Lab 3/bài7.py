n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

count = 0
for i in range(1, n + 1):
    tong_chu_so = sum(int(ch) for ch in str(i))  
    if tong_chu_so % 2 == 0:  
        count += 1

print("Có", count, "số trong khoảng [1,", n, "] có tổng chữ số là số chẵn.")