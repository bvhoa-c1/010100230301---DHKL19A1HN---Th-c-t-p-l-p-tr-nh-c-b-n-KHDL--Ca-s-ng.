def fibonacci():
    print("Dãy fibonacci (10 số đầu tiên)")
    n1, n2 = 0, 1
    for i in range(10):
        print(n1, end=" ")
        n1, n2 = n2, n1 + n2
    print()
fibonacci()