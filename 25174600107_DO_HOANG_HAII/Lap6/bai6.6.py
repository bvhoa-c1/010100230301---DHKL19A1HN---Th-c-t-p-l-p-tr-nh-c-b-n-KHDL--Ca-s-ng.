n = int(input("Nhập số lượng phần tử: "))
arr = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    arr.append(num)

if len(arr) < 2:
    print("Cần ít nhất 2 phần tử!")
else:
    differences = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    
    print(f"\nDãy số: {arr}")
    print(f"Sai phân giữa các phần tử: {differences}")
    
    if len(set(differences)) == 1:
        print(f"Dãy số là cấp số cộng với công sai d = {differences[0]}")
    else:
        print("Dãy số không phải là cấp số cộng")
