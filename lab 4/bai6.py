chuoi_n = input("Nhập n: ")
k = len(chuoi_n)  # Số lượng chữ số
n = int(chuoi_n)

tong = 0
temp = n

# Bóc tách từng chữ số từ phải sang trái
while temp > 0:
    chu_so = temp % 10
    tong += chu_so ** k
    temp //= 10

if tong == n:
    print(f"{n} là số Armstrong")
else:
    print(f"{n} không phải số Armstrong")