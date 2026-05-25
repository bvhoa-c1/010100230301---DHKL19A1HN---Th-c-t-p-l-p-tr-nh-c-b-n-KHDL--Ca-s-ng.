x = input()

thuong = hoa = so = ki_tu = 0

for fu in x:
    if fu.islower():
        thuong += 1
    elif fu.isupper():
        hoa += 1
    elif fu.isdigit():
        so += 1
    else:
        ki_tu += 1
print(thuong , hoa , so , ki_tu)





