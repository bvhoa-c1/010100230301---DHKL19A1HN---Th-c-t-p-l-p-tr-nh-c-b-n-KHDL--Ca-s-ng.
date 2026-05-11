n = int(input("n = "))
a = list(map(float, input("array = ").split()))[:n]

if not a:
    print("Empty array")
else:
    print(max(a))
    print(min(a))
