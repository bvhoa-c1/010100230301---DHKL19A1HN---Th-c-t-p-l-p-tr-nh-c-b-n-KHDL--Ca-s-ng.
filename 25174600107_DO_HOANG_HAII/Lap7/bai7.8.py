quantity = {
    'apple': 50,
    'banana': 30,
    'orange': 40,
    'grape': 25
}

unit_price = {
    'apple': 10000,
    'banana': 8000,
    'orange': 12000,
    'grape': 15000
}

print("HÓA ĐƠN CHI TIẾT")
print("=" * 60)
print(f"{'Mặt hàng':<15} {'Số lượng':<12} {'Đơn giá':<12} {'Thành tiền':<12}")
print("-" * 60)

total = 0

for item in quantity:
    qty = quantity[item]
    price = unit_price[item]
    amount = qty * price
    total += amount
    
    print(f"{item:<15} {qty:<12} {price:<12,} {amount:<12,}")

print("-" * 60)
print(f"{'TỔNG CỘNG':<40} {total:>18,}")
print("=" * 60)
