try:
	a = float(input("Nhap so a: "))
	b = float(input("Nhap so b: "))

	print(f"Tong: {a + b}")
	print(f"Hieu: {a - b}")
	print(f"Tich: {a * b}")
	if b == 0:
		print("Thuong: khong the chia cho 0")
	else:
		print(f"Thuong: {a / b}")
except ValueError:
	print("Du lieu khong hop le.")
