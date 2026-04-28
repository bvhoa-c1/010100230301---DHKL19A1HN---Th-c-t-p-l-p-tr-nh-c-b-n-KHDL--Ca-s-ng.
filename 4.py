dem = 0
tong = 0
max = 0
while True:
    n = int(input())

    if n != 0:
        dem += 1
        tong += n
        if n > max:
            max = n

    else:
        print(dem, "va", tong ,"va", max)
        break

