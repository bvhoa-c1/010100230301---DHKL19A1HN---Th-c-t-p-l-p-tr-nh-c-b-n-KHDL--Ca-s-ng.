# Bài 7: Bảng cửu chương 2-9 bằng while lồng nhau
i = 2
while i <= 9:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j}", end="  ")
        j += 1
    print()
    i += 1
