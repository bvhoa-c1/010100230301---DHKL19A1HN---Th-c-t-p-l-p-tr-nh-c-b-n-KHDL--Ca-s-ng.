a = [1, 2, 3, 4, 5, 6]

even_cube = list(
    map(lambda x: x ** 3,
        filter(lambda x: x % 2 == 0, a))
)

odd_square = list(
    map(lambda x: x ** 2,
        filter(lambda x: x % 2 != 0, a))
)

print("Chan lap phuong:", even_cube)
print("Le binh phuong:", odd_square)