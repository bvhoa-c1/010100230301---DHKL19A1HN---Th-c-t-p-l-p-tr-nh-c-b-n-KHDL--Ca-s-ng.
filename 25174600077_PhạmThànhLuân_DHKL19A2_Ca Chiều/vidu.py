#Biến cục bộ 
def my_function() :
    x=10
    print(x)
my_function()

# Biến toàn cục
x =10 
def my_function() :
    global x
    x =20 
    print(x)
my_function()

#Tham số bắt buộc 
def greet(name,age) :
    print("Hello "+ name+"! You are "+str(age)+"year olds")
greet("Aice",25)

#Thamm số mặc định 
def greet(name,age=30) :
    print("Hello "+ name+"! You are "+str(age)+"year olds")
greet("Alice")
#Tham số theo tên 

def greet(name,age) :
    print("Hello "+ name +"! You are "+str(age)+"year olds")
greet(age=25,name="Alice")

#Tham chiếu
def modify_list(lst) :
    lst.append(4)
my_list =[1,2,3]
modify_list(my_list)
print(my_list)

#tham trị 
def modify_value(x) :
    x=x+1
    print("inside function: ",x)
num=10
modify_value(num)
print("outside function:",num)