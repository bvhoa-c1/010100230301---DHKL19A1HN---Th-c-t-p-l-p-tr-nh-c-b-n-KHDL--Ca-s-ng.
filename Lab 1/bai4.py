import math
while True:
    n = int(input("nhập n(n>0):"))
    if n > 0:
        break
    print(" vui lòng nhập lai!")
s1 = sum(range(1, n + 1))
s2 = sum(1/i for i in range(1, n + 1))
s3 = sum(1/math.sqrt(2*i) for i in range(1, n + 1))
s4 = sum(((-1)**(i + 1))/i for i in range(1, n + 1))
print(f"a) s1 = {s1}")
print(f"b) s2 = {s2}")
print(f"c) s3 = {s3}")
print(f"d) s4 = {s4}")