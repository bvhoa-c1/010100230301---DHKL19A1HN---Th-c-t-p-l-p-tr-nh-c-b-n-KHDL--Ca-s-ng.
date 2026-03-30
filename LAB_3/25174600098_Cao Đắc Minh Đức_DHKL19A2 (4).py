import math
n = int(input("nhập số nguyên dương n: "))
if n>0:
 print("n phải là số nguyên dương, vui lòng nhập lại.")
 #caua s1 = 1 + 2 + ... + n
 s1 = sum(range(1, n+ 1))
print("s1= ", s1 )
#caub s2 = 1/1 + 1/2 +1/3 + ... + 1/n
s2 = sum(1/i for i in range(1, n + 1))
print("s2 =", s2)
#cauc 1/sqrt(2) + 1/sqrt(4) + 1/sqrt(6) + ... + 1/sqrt(2n)
s3 = sum(1/math.sqrt(2*i) for i in range (1,n+1))
print("s3 =", s3)
#caud 1/1 - 1/2 + 1/3 - 1/4 + ... + (-1)^(n+1)/n
s4 = sum(((-1)**(i+1))/i for i in range(1, n+1))
print("s4 = ", s4)