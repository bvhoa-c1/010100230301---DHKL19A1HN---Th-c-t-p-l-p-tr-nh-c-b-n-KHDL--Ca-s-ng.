nhap = input("nhap day so")
day_so = []
for x in nhap :
    if '.' in x:
        day_so.append(float(x))
    else:
        day_so.append(int(x))
print(day_so)
print(max(day_so))
print(min(day_so))
