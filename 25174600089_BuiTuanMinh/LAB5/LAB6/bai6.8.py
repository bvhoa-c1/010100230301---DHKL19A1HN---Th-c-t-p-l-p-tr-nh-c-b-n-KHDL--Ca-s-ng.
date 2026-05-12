m1 = int(input("so hang "))
n1=int(input("so cot"))
A=[list(map(int, input(i+1).split()))]
m2=int(input("so hang"))
n2=int(input("so cot "))
B=[list(map(int,input(i+1).split()))]
if n1 != m2:
    print("ko the nhan")
else:
    C=[]
    for i in range(m1):
        hang=[]
        for j in range (n2):
            tong=0
            for k in range(n1):
                tong+= A[i][k] * B[k][j]
            hang.append(tong)
        C.append(hang)
    print(hang)
    