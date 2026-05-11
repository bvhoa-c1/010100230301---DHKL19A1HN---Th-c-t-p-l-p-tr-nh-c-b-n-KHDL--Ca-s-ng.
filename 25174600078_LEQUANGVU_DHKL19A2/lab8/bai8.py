arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

chan = list(filter(lambda x: x % 2 == 0, arr))
le = list(filter(lambda x: x % 2 != 0, arr))

print("So chan:", chan)
print("So le:", le)