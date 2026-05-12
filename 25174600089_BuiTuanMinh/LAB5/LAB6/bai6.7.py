m = input("nhap m:")
n = input("nhap n:")
ma_tran=[]
for i in range(m):
    hang= list(map(int, input(i+1)))
    ma_tran.append(hang)
tong=0
for hang in ma_tran():
    for phan_tu in hang:
        tong+= phan_tu
print(tong)
