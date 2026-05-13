inventory = {
    'apple': 50,
    'banana': 30,
    'orange': 40,
    'grape': 25,
    'mango': 35
}

print("Tồn kho ban đầu:")
print(f"{'Mặt hàng':<15} {'Số lượng':<12}")
print("-" * 27)
for item, qty in inventory.items():
    print(f"{item:<15} {qty:<12}")

print("\n" + "=" * 27)

n = int(input("Nhập số lượng giao dịch: "))

for i in range(n):
    item = input(f"\nGiao dịch {i+1} - Nhập tên mặt hàng: ").lower()
    quantity_sold = int(input(f"Nhập số lượng bán: "))
    
    if item in inventory:
        if inventory[item] >= quantity_sold:
            inventory[item] -= quantity_sold
            print(f"Đã bán {quantity_sold} {item}. Còn lại: {inventory[item]}")
        else:
            print(f"Không đủ hàng! Chỉ còn {inventory[item]} {item}")
    else:
        print(f"Không tìm thấy mặt hàng '{item}'")

print("\n" + "=" * 27)
print("Tồn kho cập nhật:")
print(f"{'Mặt hàng':<15} {'Số lượng':<12}")
print("-" * 27)
for item, qty in inventory.items():
    print(f"{item:<15} {qty:<12}")
