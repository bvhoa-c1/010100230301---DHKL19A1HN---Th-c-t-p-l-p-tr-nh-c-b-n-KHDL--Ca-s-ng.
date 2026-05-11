print("Nhap ma tran 2x2")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

det = a * d - b * c

if det == 0:

    print("Ma tran khong kha nghich")

else:

    print("Ma tran nghich dao:")

    print(f"{d/det}   {-b/det}")
    print(f"{-c/det}   {a/det}")