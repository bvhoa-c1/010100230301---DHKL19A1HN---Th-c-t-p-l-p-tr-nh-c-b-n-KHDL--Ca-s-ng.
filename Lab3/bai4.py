import math

n = int(input("Nhập n : "))
if n <= 0 :
    print("Nhập lại n (n > 0 ) : ")
else : 
    S1=S2=S3=S4=0
    for i in range(1,n+1) :
        S1+=i
        S2+=1/i
        S3+=1/(math.sqrt(i+1))
        S4+=((-1)**(i+1))/i
print(f"a) S1={S1}")
print(f"b) S2={S2}")
print(f"c) S3={S3}")
print(f"d) S4={S4}")


