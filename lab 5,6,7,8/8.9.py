# Dùng map và filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_cubes = list(map(lambda x: x ** 3,
                      filter(lambda x: x % 2 == 0, numbers)))

odd_squares = list(map(lambda x: x ** 2,
                       filter(lambda x: x % 2 != 0, numbers)))

print("Lập phương số chẵn:", even_cubes)
print("Bình phương số lẻ:", odd_squares)