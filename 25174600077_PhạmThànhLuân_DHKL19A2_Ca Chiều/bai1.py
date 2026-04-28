def luy_thua() :
    a = int(input("Nhập số : "))
    n = int(input("Nhập số mũ : "))
    ket_qua = 1
    for i in range(n) :
        ket_qua*=a
    print(f"{a}^{n}={ket_qua}")
luy_thua()
