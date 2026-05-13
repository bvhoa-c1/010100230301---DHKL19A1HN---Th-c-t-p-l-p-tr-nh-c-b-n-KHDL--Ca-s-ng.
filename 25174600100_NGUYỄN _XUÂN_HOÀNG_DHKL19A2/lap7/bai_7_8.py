# Bài 7.8: Tính chi phí và in hóa đơn chi tiết

# Từ điển số lượng tồn kho
inventory = {
    'apple': 10,
    'banana': 8,
    'orange': 5,
    'mango': 3
}

# Từ điển đơn giá
prices = {
    'apple': 1.5,
    'banana': 2.0,
    'orange': 2.5,
    'mango': 3.0
}

# Tính chi phí cho mỗi mặt hàng
print("=" * 50)
print("HÓA ĐƠN CHI TIẾT")
print("=" * 50)
print(f"{'Mặt hàng':<15} {'SL':<5} {'Đơn giá':<10} {'Thành tiền':<15}")
print("-" * 50)

total_cost = 0

for item in inventory:
    quantity = inventory[item]
    unit_price = prices[item]
    total = quantity * unit_price
    total_cost += total
    
    print(f"{item:<15} {quantity:<5} {unit_price:<10.2f} {total:<15.2f}")

print("-" * 50)
print(f"{'TỔNG CỘNG':<30} {total_cost:>15.2f}")
print("=" * 50)
