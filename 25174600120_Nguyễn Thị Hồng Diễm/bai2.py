def in_fibonacci_10():
    max_terms = 10
    a, b = 0, 1

    if max_terms >= 1:
        print(a, end='')
    if max_terms >= 2:
        print(' ', b, end='')

    for _ in range(3, max_terms + 1):
        c = a + b
        print(' ', c, end='')
        a, b = b, c

    print()  # xuống dòng cuối cùng

if __name__ == "__main__":
    in_fibonacci_10()

