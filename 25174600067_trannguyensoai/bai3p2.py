import math

def tinh_hinh_tron(r):
    chu_vi = 2 * math.pi * r
    dien_tich = math.pi * r * r
    return chu_vi, dien_tich

# Nhập bán kính
r = float(input("Nhập bán kính: "))

# Tính toán
cv, dt = tinh_hinh_tron(r)

# In kết quả
print("Chu vi:", cv)
print("Diện tích:", dt)