numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print("Bình phương các số chẵn:")
print(result)