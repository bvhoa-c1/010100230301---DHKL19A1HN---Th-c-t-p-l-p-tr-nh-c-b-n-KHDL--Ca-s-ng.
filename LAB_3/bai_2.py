# In bảng cửu chương từ 1 đến 9 dạng bảng 2 chiều

print("   ", end="")
for j in range(1, 10):
    print(f"{j:4d}", end="")
print()

for i in range(1, 10):
    print(f"{i:2d} ", end="")
    for j in range(1, 10):
        print(f"{i*j:4d}", end="")
    print()
