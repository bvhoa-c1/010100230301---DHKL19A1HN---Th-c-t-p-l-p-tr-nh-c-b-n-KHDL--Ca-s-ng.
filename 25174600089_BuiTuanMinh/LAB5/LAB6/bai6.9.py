m = int(input("so hang"))
n=int(input("so cot"))
A= [list(map(int,input(i+1).split()))]
chuyen_vi=[]
for j in range(n):
    hang_moi=[]
    for i in range (m):
        hang_moi.append(A[i][j])
    chuyen_vi.append(hang_moi)
print("ma tran goc")
for hang in A:
    print(" ", hang)
print("ma trann chuyen vi")
for hang in chuyen_vi:
    print(" ", hang)
if m ==n:
    doi_xung = True
    for i in range(m):
        for j in range(n):
            if A[i][j]!=A[j][i]:
                doi_xung= False
                break
    if doi_xung:
        print("la ma  tran doi xung")
    else:
        print("ko la ma tran doi xung")
else:
    print("ma tran ko  vuong")
    