n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhập số: ")))
diff = arr[1] - arr[0]
is_ap = True
for i in range(2, n):
    if arr[i] - arr[i-1] != diff:
        is_ap = False
        break
if is_ap:
    print("Là cấp số cộng")
else:
    print("Không là cấp số cộng")