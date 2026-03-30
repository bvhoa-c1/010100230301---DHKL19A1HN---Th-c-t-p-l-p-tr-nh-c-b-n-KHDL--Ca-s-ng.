n = int(input("Nhập n: "))
temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if rev == n:
    print("Đúng")
else:
    print("Sai")