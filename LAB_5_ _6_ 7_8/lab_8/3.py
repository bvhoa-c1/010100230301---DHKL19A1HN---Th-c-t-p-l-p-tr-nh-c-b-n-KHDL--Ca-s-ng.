n, k = map(int, input().split())
if n < k:
    exit()
def tinh_toan(n, k):
    tu = mau = k_gt = 1
    for i in range(1, n + 1):
        tu *= i

    for j in range(1, k + 1):
        k_gt *= j

    for f in range(1, n - k + 1):
        mau *= f

    chinh_hop = tu / mau
    to_hop = tu / (mau * k_gt)

    return chinh_hop, to_hop

print("chinh hop , to hop")
print(tinh_toan(n, k))