import math

def tinh_chu_vi(r):
    return 2 * math.pi * r

def tinh_dien_tich(r):
    return math.pi * r * r

r = float(input("Nhập bán kính r: "))

print("Chu vi =", tinh_chu_vi(r))
print("Diện tích =", tinh_dien_tich(r))