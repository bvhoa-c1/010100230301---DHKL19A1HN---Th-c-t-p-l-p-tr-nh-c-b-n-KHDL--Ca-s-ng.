arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

chan = list(map(lambda x: x ** 3,
                filter(lambda x: x % 2 == 0, arr)))

le = list(map(lambda x: x ** 2,
              filter(lambda x: x % 2 != 0, arr)))

print("Lap phuong so chan:", chan)
print("Binh phuong so le:", le)