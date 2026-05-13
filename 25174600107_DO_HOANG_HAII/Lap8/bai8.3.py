def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutation(n, r):
    if n < 0 or r < 0 or r > n:
        return None
    return factorial(n) // factorial(n - r)

def combination(n, r):
    if n < 0 or r < 0 or r > n:
        return None
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Nhập n: "))
r = int(input("Nhập r: "))

if n < 0 or r < 0 or r > n:
    print("Giá trị n, r không hợp lệ!")
else:
    perm = permutation(n, r)
    comb = combination(n, r)
    
    print(f"\nHoán vị P({n},{r}) = {perm}")
    print(f"Tổ hợp C({n},{r}) = {comb}")
