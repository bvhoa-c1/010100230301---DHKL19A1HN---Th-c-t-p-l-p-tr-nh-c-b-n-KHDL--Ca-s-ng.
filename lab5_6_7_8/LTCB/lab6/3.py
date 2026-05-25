a = list(map(float, input().split()))
min = 0
max = 0
for i in a:
    if max <= i:
        max = i
    if min >= i:
        min = i
print("min va max lan luot", min, max)