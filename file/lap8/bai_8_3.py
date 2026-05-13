# Bài 8.3: Hàm tính hoán vị và tổ hợp

def factorial(n):
    """Tính giai thừa của n"""
    if n < 0:
        raise ValueError("Giai thừa không xác định cho số âm!")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutation(n, r):
    """Tính số hoán vị P(n, r) = n! / (n-r)!"""
    if n < 0 or r < 0:
        raise ValueError("n và r phải không âm!")
    if r > n:
        raise ValueError("r không thể lớn hơn n!")
    
    return factorial(n) // factorial(n - r)

def combination(n, r):
    """Tính số tổ hợp C(n, r) = n! / (r! * (n-r)!)"""
    if n < 0 or r < 0:
        raise ValueError("n và r phải không âm!")
    if r > n:
        raise ValueError("r không thể lớn hơn n!")
    
    return factorial(n) // (factorial(r) * factorial(n - r))

# Kiểm tra các hàm
print("HOÁN VỊ VÀ TỔ HỢP")
print("=" * 50)

try:
    n = int(input("Nhập n: "))
    r = int(input("Nhập r: "))
    
    if n >= 0 and r >= 0:
        perm = permutation(n, r)
        comb = combination(n, r)
        
        print(f"\nHoán vị P({n}, {r}) = {perm}")
        print(f"Tổ hợp C({n}, {r}) = {comb}")
        
        # Bảng hoán vị và tổ hợp
        print(f"\nBảng hoán vị P({n}, r):")
        for i in range(n + 1):
            print(f"P({n}, {i}) = {permutation(n, i)}", end="  ")
        
        print(f"\n\nBảng tổ hợp C({n}, r):")
        for i in range(n + 1):
            print(f"C({n}, {i}) = {combination(n, i)}", end="  ")
    else:
        print("n và r phải không âm!")
        
except ValueError as e:
    print(f"Lỗi: {e}")
except Exception as e:
    print(f"Lỗi: {e}")
