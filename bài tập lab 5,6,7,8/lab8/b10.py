arr = [1, 2, 3, 4, 5]
even_cubes = []
odd_squares = []
for x in arr:
    if x % 2 == 0:
        even_cubes.append(x**3)
    else:
        odd_squares.append(x**2)
print("Lập phương chẵn:", even_cubes)
print("Bình phương lẻ:", odd_squares)