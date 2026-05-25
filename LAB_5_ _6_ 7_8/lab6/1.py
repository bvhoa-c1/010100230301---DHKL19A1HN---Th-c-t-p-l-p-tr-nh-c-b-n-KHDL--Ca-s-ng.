a = list(map(int, input().split()))
chan = []
le = []
for i in a:
    if i % 2 == 0:
        chan.append(i)
    else:
        le.append(i)
print("list chan", chan)
print("tong chan", sum(chan))
print("list le", le)
print("tong le", sum(le))