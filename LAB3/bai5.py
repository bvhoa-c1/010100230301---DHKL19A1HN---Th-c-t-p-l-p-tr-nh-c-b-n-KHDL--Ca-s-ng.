import math
print("Cac so chinh phuong tu 1 den 1000:")
squares = [i for i in range(1, 1001) if math.isqrt(i)**2 == i]
print(' '.join(map(str, squares)))
