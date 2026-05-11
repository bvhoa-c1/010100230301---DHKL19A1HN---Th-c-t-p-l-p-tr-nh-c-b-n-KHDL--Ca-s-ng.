ds_so = list(map(float, input("Nhập dãy số: ").split()))
if ds_so:
    max = ds_so[0]
    min = ds_so[0]
    for i in ds_so:
        if i > max:
            max = i
        if i < min:
            min = i
    print(f"Max: {max}, Min: {min}")