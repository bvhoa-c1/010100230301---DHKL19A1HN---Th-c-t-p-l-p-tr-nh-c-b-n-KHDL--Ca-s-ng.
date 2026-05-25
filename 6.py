a = list(map(int, input().split()))
if len(a) < 2:
    exit()
else:
    d = a[2] - a[1]
for i in range(1, (len(a) - 1)):
    if a[i + 1] - a[i] != d:
        print("k p csc")
        break

else:
    print("csc")

