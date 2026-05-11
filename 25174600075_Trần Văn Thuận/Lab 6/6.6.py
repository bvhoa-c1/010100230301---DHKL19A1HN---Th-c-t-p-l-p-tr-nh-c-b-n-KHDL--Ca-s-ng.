n = int(input("Nhập số lượng phần tử: "))
ds = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(x)
if n < 2:
    print("Không đủ phâng tử")
else:
    hieu = ds[1] - ds[0]
    cap_so_cong = True
    for i in range(1, n-1):
        if ds[i+1]-ds[i] != hieu:
            cap_so_cong = False
            break
    if cap_so_cong:
        print("đây là cấp số cộng")
    else:
        print("Không phải cấp số cộng")