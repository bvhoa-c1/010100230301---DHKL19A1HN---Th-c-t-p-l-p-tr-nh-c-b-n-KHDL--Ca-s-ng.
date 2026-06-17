chuoi = input("nhap chuoi:")
chu_thuong= 0 
chu_hoa = 0
chu_so=0
dac_biet=0
for ky_tu in chuoi:
    if ky_tu.islower():
        chu_thuong+=1
    elif ky_tu.isupper():
        chu_hoa+=1
    elif ky_tu.isdigit():
        chu_so+=1
    else:
        dac_biet+=1
print(chu_thuong)
print(chu_hoa)
print(chu_so)
print(dac_biet)