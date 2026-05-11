n = int(input("n = "))
a = list(map(int, input("array = ").split()))[:n]

even = [x for x in a if x % 2 == 0]
odd = [x for x in a if x % 2 != 0]

print(even, sum(even))
print(odd, sum(odd))
