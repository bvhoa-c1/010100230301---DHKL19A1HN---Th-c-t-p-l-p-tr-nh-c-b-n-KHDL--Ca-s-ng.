def modify_list(lst):
    lst.append(4)
my_list = [1,2,3]
modify_list(my_list)
print(my_list)

def modify_value(x):
    x += 1
    print("ínide function:", x)
num = 10
modify_value(num)
print("outside function:", num)