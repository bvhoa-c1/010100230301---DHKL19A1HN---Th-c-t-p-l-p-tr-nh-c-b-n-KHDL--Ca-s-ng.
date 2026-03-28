n = input("Nhập số n: ")
S = 0
k = len(n)

for i in n:
    S += int(i)**k

if S == int(n):
    print("Đúng")
else:
    print("Sai")
