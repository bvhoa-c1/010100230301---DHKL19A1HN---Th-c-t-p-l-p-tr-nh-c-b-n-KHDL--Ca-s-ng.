n = int(input('nhập số nguyên dương: '))
dem = 0
a = 0
for i in range(1, n + 1):
    a = sum( int(j) for j in str(i) )
    if a % 2 == 0:
        dem += 1
print(dem)