n = int(input())
lat = 0
a = n
while n != 0:
    lat = lat * 10 + n % 10
    n //= 10
print(lat)
if a == lat :
    print("so doi xung")
else:
    print("k p so doi xung")