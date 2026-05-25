x = "r436768"
a = ""
for i in x:
    if i.isdigit():
        a += i
b = int(a)
print(b , type(b))
for j in range(2, b):
    if b % j == 0:
        print("k p snt")
        break
else:
    print("snt")

