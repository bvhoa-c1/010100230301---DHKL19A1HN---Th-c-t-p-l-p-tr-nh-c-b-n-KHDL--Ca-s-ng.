n = int(input("Nhập n: "))
temp = n
sum_arm = 0
p = len(str(n))
while temp > 0:
    chu_so = temp % 10
    sum_arm += chu_so ** p
    temp //= 10

if n == sum_arm:
    print(f"{n} là số Armstrong")
else:
    print(f"{n} không phải số Armstrong")