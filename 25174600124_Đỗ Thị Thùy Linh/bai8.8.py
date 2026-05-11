a = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda x: x % 2 == 0, a))
odd = list(filter(lambda x: x % 2 != 0, a))

print("So chan:", even)
print("So le:", odd)