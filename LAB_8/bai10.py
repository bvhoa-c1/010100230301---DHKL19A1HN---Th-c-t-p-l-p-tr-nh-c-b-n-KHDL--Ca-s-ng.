numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(map(lambda x: x**3,
                filter(lambda x: x % 2 == 0, numbers)))

odd = list(map(lambda x: x**2,
               filter(lambda x: x % 2 != 0, numbers)))

print("Lap phuong so chan:", even)
print("Binh phuong so le:", odd)