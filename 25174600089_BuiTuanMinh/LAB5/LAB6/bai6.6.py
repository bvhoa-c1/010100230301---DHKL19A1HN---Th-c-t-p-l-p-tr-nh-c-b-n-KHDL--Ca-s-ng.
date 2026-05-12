nhap = input("nhap so nguyen")
day = [int(x)for x in nhap]
sai_phan = []
for i in range(len(day)-1):
    sai_phan.append(day[i+1]- day[i])
print(day)
print(sai_phan)
if len(set(sai_phan))==1:
    print(sai_phan[0])
else:
    print("day ko phải cap  so cong")
    