import math
while True:
    n = int(input('nhập số nguyên dương:  '))
    if n >= 0:
        print(sum(i for i in range(1, n + 1)))
        print(sum(1 / i for i in range(1, n + 1)))
        print(sum(1 / math.sqrt(2 * i) for i in range(1, n + 1)))
        print(sum(((-1)**i + 1) / i for i in range(1, n + 1)))
        break
    else:
        print('nhập số nguyên dương')