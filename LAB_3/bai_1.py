# Chương trình tính tổng các số chia hết cho 7 nhưng không chia hết cho 5 từ 2000 đến 4000
#a
tonga = 0
for i in range(2000, 4000):
    if i % 7 == 0 and i % 5 != 0:
        tonga += i

print("Tổng  a là:", tonga)
#b
tongb=0
for a in range(500,1000):
    if a%4==0 and a%6!=0:
        tongb +=a
print("Tổng b là:", tongb)
