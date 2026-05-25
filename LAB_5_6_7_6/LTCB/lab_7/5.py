ver = input()
for i in ",.?:;":
    ver = ver.replace(i, "")
ver = ver.lower()

liet_ke = {}

tach = ver.split()
for j in tach:
    if j in liet_ke:
        liet_ke[j] += 1
    else:
        liet_ke[j] = 1
M = max(liet_ke, key=liet_ke.get)

m = min(liet_ke, key=liet_ke.get)
print(M , liet_ke[M])
print(m , liet_ke[m])



