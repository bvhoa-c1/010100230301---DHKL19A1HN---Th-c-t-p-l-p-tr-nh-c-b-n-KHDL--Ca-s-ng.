import math


try:
	r = float(input("Nhap ban kinh r: "))
	if r < 0:
		print("Ban kinh khong hop le.")
	else:
		chu_vi = 2 * math.pi * r
		dien_tich = math.pi * r * r
		print(f"Chu vi: {chu_vi}")
		print(f"Dien tich: {dien_tich}")
except ValueError:
	print("Du lieu khong hop le.")
