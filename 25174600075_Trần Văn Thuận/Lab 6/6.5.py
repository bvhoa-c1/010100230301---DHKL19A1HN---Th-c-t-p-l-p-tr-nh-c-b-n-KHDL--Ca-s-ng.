so_ngto = [x for x in range(2, 100)
           if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
print("các số nguyên tố nhỏ hơn 100")
print(so_ngto)
