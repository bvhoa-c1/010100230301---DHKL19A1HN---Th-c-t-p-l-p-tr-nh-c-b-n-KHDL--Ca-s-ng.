import math
n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Yêu cầu nhập lại.")
else:
    S1 = 0
    S2 = 0
    S3 = 0
    S4 = 0
    for i in range(1,n+1):
        S1 += i
        S2 += 1/i
        S3 += 1/math.sqrt(2*i)
        if i%2==0:
            S4 = S4 - (1/i) # Nếu i chẵn thì trừ đi
        else:
            S4 = S4 + (1/i) # Nếu i lẻ thì cộng vào
print("S1 = ",S1)
print("S2 = ",round(S2,2))
print("S3 = ",round(S3,2))
print("S4 = ",round(S4,2))