import math

def chu_vi(r):
    return 2 * math.pi * r

def dien_tich(r):
    return math.pi * r * r

r = float(input("Nhập bán kính r: "))

print("Chu vi:", chu_vi(r))
print("Diện tích:", dien_tich(r))