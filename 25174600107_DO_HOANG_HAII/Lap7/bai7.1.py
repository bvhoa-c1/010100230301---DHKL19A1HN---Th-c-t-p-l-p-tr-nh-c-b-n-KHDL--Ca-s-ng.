n = int(input("Nhập số nguyên N: "))

dictionary = {x: x**3 for x in range(1, n + 1)}

print(f"Từ điển với khóa là x và giá trị là x³:")
print(dictionary)
