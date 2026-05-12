x = 10 # Biến toàn cục 
def my_function():
 global x #Khai báo biến đó là biến toàn cục
 x = 20
print(x)
my_function() # Kết quả: 20 (giá trị biến toàn cục được thay đổi)
print(x) # Kết quả: 20 (giá trị biến toàn cục đã được thay đổi)