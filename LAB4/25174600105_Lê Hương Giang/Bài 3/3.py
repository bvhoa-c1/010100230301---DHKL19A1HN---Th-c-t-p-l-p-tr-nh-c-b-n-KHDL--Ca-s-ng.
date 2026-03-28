n = int(input("Nhập số n: "))

for i in range(n-1,0,-1):
    if n%i==0:
        print("Uớc số lớn nhất của n (khác n): ",i)
        break