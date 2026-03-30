n = int(input())
uoc_max = 1
i = 1
while i < n:
    if n % i == 0:
        uoc_max = i
    i += 1
print(uoc_max)