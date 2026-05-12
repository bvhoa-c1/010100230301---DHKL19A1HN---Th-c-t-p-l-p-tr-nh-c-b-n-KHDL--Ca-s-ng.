n = int(input("nhap n"))
mang = []
for i in range(n):
    x = int(input(i+1))
    mang.append(x)

so_chan= []
so_le=[]
for x in mang:
    if x% 2 ==0:
        so_chan.append(x)
    else:
        so_le.append(x)
print(so_chan,sum(so_chan))
print(so_le,sum(so_le))
