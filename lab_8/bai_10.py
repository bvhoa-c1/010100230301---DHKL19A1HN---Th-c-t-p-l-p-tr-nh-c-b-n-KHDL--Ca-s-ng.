a = list(map(int, input("array = ").split()))

even_cubes = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, a)))
odd_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, a)))

print(even_cubes)
print(odd_squares)
