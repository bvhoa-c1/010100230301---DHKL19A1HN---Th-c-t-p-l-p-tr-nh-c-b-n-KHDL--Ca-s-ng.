try:
	n = int(input("Nhap so nguyen duong n: "))
	if n <= 0:
		print("n phai la so nguyen duong.")
	else:
		print("Cac uoc so cua n:")
		for i in range(1, n + 1):
			if n % i == 0:
				print(i)
except ValueError:
	print("Du lieu khong hop le.")
