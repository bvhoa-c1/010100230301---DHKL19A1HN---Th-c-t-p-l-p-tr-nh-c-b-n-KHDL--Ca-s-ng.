n = int(input("Nhập n: "))
temp = n
tong = 0
k = len(str(n))

while temp > 0:
    d = temp % 10
    tong += d**k
    temp //= 10

if tong == n:
    print("Là Armstrong")
else:
    print("Không phải")