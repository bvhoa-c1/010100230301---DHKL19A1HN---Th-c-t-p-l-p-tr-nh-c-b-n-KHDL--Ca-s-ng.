x = str(input())
dem = 0
for i in x:
    if "0" <= i <= "9":
        dem +=1
t = (dem / len(x)) * 100
print(t)