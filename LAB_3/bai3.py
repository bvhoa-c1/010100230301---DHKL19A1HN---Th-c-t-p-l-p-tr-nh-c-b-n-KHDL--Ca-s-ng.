# Chương trình vẽ tam giác vuông rỗng theo số hàng nhập vào

n = int(input("Nhập số hàng: "))

for i in range(1, n+1):
    if i <= 2 or i == n:
        print('*' * i)
    else:
        print('*' + ' ' * (i - 2) + '*')
