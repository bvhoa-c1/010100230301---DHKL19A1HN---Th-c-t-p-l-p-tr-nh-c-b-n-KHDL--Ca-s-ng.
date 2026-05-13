# Bài 7.9: Khấu trừ số lượng vật phẩm và in báo cáo tồn kho

# Từ điển tồn kho
inventory = {
    'apple': 50,
    'banana': 30,
    'orange': 25,
    'mango': 15,
    'grape': 20
}

# Từ điển đơn giá
prices = {
    'apple': 1.5,
    'banana': 2.0,
    'orange': 2.5,
    'mango': 3.0,
    'grape': 2.0
}

print("TỒN KHO BAN ĐẦU:")
print("-" * 40)
for item, qty in inventory.items():
    print(f"{item:<15}: {qty:>5} đơn vị")

# Nhập giao dịch
print("\n" + "=" * 40)
print("GIAO DỊCH:")
print("=" * 40)

while True:
    item = input("Nhập tên mặt hàng (hoặc 'exit' để thoát): ").lower()
    
    if item == 'exit':
        break
    
    if item not in inventory:
        print(f"Mặt hàng '{item}' không có trong kho!")
        continue
    
    try:
        quantity = int(input(f"Số lượng cần giao: "))
        
        if quantity <= 0:
            print("Số lượng phải lớn hơn 0!")
            continue
        
        if quantity > inventory[item]:
            print(f"Không đủ hàng! Tồn kho: {inventory[item]}")
            continue
        
        inventory[item] -= quantity
        print(f"✓ Giao thành công {quantity} {item}")
        
    except ValueError:
        print("Nhập số lượng không hợp lệ!")

# In báo cáo tồn kho cập nhật
print("\n" + "=" * 40)
print("BÁNG CÁO TỒN KHO CẬP NHẬT:")
print("=" * 40)
print(f"{'Mặt hàng':<15} {'Số lượng':<10} {'Đơn giá':<10} {'Giá trị kho':<15}")
print("-" * 50)

total_value = 0

for item in sorted(inventory.keys()):
    qty = inventory[item]
    unit_price = prices[item]
    value = qty * unit_price
    total_value += value
    
    print(f"{item:<15} {qty:<10} {unit_price:<10.2f} {value:<15.2f}")

print("-" * 50)
print(f"{'TỔNG GIÁ TRỊ KHO':<35} {total_value:>13.2f}")
print("=" * 50)
