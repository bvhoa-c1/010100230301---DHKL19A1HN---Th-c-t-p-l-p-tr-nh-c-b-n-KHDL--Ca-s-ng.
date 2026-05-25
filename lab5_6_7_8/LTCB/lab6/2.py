a = list(map(int, input().split()))
for i in a:
    nghiem = []
    for j in range(1,i):
        if i % j == 0:
            nghiem.append(j)
    if sum(nghiem) == 1:
        print("snt", i )
    elif sum(nghiem) == i:
        print("so hoan hao" , i )









