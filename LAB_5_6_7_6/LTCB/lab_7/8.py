nha_kho = { "gao" : 324, "nc mam" : 34, "nc dong chai" : 323, "dau goi" : 532 }
vlue = {"gao" : 100 , "nc mam" : 18, "nc dong chai" : 38, "dau goi" : 5 }
print(" "*15, "HÓA ĐƠN", " "*15)
thanh_tien = 0
all = 0
for i in nha_kho:
    vat_pham = nha_kho[i]
    gia_tri = vlue[i]
    thanh_tien = vat_pham * gia_tri
    all += thanh_tien
    print("vat pham", i, "so luong" , vat_pham,  "gia tri" , gia_tri , "thanh toan" ,thanh_tien)
print("cái gia phai tra" ,all)
