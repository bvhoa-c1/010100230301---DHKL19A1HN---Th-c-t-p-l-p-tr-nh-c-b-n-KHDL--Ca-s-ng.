# Bài 6.3: Tìm max và min trong dãy hỗn hợp

n = int(input("Nhập số phần tử của mảng: "))
arr = []

print("Nhập các số (nguyên hoặc thực):")
for i in range(n):
    num = float(input(f"Phần tử {i+1}: "))
    arr.append(num)

if arr:
    max_value = max(arr)
    min_value = min(arr)
    
    print(f"\nMảng nhập vào: {arr}")
    print(f"Giá trị lớn nhất: {max_value}")
    print(f"Giá trị nhỏ nhất: {min_value}")
else:
    print("Mảng rỗng!")
