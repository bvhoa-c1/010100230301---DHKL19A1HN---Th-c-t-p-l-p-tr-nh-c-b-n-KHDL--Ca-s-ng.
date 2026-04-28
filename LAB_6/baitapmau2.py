def in_day_fibonacci():
    a, b = 0, 1
    for i in range(10):
        print(a, end="")
        if i < 9:
            print(", ", end="")
        a, b = b, a + b
    print()
if __name__ == "__main__":
    in_day_fibonacci()

