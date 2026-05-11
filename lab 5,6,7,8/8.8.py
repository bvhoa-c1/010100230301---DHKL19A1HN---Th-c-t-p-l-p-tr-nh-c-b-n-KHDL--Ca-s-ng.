# Tách số chẵn và số lẻ bằng filter + lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))

print("Số chẵn:", even)
print("Số lẻ:", odd)