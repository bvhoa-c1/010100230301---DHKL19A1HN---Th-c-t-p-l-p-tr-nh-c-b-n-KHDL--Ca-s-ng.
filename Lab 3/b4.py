import math
n = int(input("Nhập n (>0): "))
while n <= 0:
    n = int(input("Nhập lại n: "))

#a
s1 = 0
for i in range(1, n+1):
    s1 += i

#b
s2 = 0
for i in range(1, n+1):
    s2 += 1/i

#c
s3 = 0
for i in range(1, n+1):
    s3 += 1/math.sqrt(2*i)

#d
s4 = 0
for i in range(1, n+1):
    s4 += ((-1)**(i+1))/i
print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
print("s4 =", s4)