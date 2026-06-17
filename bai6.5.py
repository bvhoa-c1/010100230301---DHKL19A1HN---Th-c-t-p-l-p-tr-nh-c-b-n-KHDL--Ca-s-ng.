# Tạo danh sách số nguyên tố nhỏ hơn 100 bằng List Comprehension

so_nguyen_to = [n for n in range(2, 100)
                if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]

print("Danh sách số nguyên tố nhỏ hơn 100:")
print(so_nguyen_to)