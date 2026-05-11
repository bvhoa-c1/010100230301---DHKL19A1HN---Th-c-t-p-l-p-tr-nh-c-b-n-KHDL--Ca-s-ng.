n = int(input("n = "))

if n <= 0:
    print("n must be positive")
else:
    print(bin(n)[2:])
