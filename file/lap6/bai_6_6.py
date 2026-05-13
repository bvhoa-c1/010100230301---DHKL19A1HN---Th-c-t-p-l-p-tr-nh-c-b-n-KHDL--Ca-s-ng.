# Bài 6.6: Kiểm tra dãy có phải cấp số cộng

n = int(input("Nhập số phần tử của dãy: "))
arr = []

print("Nhập các số nguyên:")
for i in range(n):
    num = int(input(f"Phần tử {i+1}: "))
    arr.append(num)

print(f"\nDãy nhập vào: {arr}")

if len(arr) < 2:
    print("Dãy quá ngắn để kiểm tra!")
else:
    # Tính sai phân giữa các phần tử liên tiếp
    differences = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    print(f"Sai phân: {differences}")
    
    # Kiểm tra tất cả sai phân có bằng nhau không
    if len(set(differences)) == 1:
        print(f"✓ Dãy là cấp số cộng với công sai d = {differences[0]}")
    else:
        print("✗ Dãy không phải cấp số cộng")
