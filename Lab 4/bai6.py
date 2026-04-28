n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

chu_so = str(n)
k = len(chu_so)  
tong = 0

for ch in chu_so:
    tong += int(ch) ** k

if tong == n:
    print(n, "là số Armstrong.")
else:
    print(n, "không phải là số Armstrong.")