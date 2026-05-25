nha_kho = {"gao" : 324 , "nc mam" : 34 , "nc dong chai" : 323 , "dau goi" : 532 }
vlue = {"gao" : 100 , "nc mam" : 18 , "nc dong chai" : 36 , "dau goi" : 8}
khach_mua = {"gao" : 64 , "nc dong chai" : 33 }
thanh_toan = 0
hi = 0
for i in khach_mua:
    mua = khach_mua[i]
    if mua <= nha_kho[i]:
        do = khach_mua[i]
        gtri = vlue[i]
        thanh_toan = do * gtri
        # khau tru
        nha_kho[i] -= mua
    else:
        print("erorr")
    hi += thanh_toan
    print("khach mua" , i , "so Luong" , do , "gia_tri" , vlue , "so tien" , thanh_toan)
print("all" , hi)
print("con nhung hang", nha_kho)








