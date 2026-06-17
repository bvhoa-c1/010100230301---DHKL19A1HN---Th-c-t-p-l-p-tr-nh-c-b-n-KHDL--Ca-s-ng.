chuoi = input("nhap chuoi:")
tong = len(chuoi)
if tong == 0:
    print("chuoi rỗng")
else:
    dac_biet = {}
    for ky_tu in chuoi:
        if not ky_tu.isalpha() and not ky_tu.isdigit():
            dac_biet[ky_tu]= dac_biet.get(ky_tu, 0 )+1
    if dac_biet:
        print("ky tu dac biet")
        for ky_tu, so_lan in dac_biet.items():
            phan_tram = so_lan/ tong*100
            print(ky_tu,so_lan,"->",phan_tram)
    else:
        print("ko có ký tự dặc biệt")
