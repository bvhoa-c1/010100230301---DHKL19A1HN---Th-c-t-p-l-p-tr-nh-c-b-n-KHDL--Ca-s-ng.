n = int(input("Nhập n: "))
temp = n
digits = len(str(n))
s = 0
while temp > 0:
    d = temp % 10
    s += d ** digits
    temp //= 10
if s == n:
    print("Đúng")
else:
    print("Sai")