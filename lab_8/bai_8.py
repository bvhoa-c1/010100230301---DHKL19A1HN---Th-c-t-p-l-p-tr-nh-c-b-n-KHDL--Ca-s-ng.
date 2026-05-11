a = list(map(int, input("array = ").split()))

even = list(filter(lambda x: x % 2 == 0, a))
odd = list(filter(lambda x: x % 2 != 0, a))

print(even)
print(odd)
