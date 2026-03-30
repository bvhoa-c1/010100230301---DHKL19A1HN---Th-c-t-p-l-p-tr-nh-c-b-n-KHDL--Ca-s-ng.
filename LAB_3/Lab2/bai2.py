print("   ", end="")
for j in range(1, 10):
    print(f"{j:4}", end="")
print()
for i in range(1, 10):
    print(f"{i:2} ", end="")
    for j in range(1, 10):
        print(f"{i*j:4}", end="")
    print()