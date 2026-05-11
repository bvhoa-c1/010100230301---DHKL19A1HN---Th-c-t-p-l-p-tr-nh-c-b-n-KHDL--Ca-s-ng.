n = int(input("Nhap n = "))
 
A = []
for i in range(n):
    hang = list(map(float, input().split()))
    A.append(hang)

if n == 2:
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    det = a * d - b * c
    if det == 0:
        print("Ma tran khong kha nghich")
    else:
        print("Ma tran nghich dao la:")
        B = [
            [ d/det , -b/det ],
            [ -c/det , a/det ]
        ]
        for i in B:
            print(tuple(i))
else:
    print("Chi ap dung cho ma tran 2x2")