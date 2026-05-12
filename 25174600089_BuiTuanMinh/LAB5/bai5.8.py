nguon = input("nhap chuoi ban dau:")
dich= input("nhap chuoi muc tieu:")

ds = list(nguon)
dt = list(dich)
cac_buoc= []
i = 0 
j= 0
while i <len(ds)or j < len(dt):
    if i < len(ds) and j < len(dt):
        if ds[i]== dt[j]:
            i +=1
            j+=1
        else:
            cac_buoc.append(f"thay'{dt[i]}'->'{dt[j]}'tại {i}")
            ds[i] = dt[j]
            i +=1
            j+=1
    elif j < len(dt):
        cac_buoc.append("thêm",ds[i],"tại",{i})
        ds.insert(i , dt[j])
        i+=1
        j+=1
    else:
        cac_buoc.append("xóa",ds[i],"tại",{i})
        ds.pop(i)
print("".join(ds))
    