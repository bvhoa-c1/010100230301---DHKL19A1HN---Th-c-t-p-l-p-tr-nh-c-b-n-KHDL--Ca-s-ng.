#vd1,
x = 10
def my_function():
    global x
    x = 20
    print(x)
my_function()
print(x)
#vd2,
def greet(name,age=30):
    print("Hello,"+name+"!You are "+str(age)+" year old")
greet("Alice")
greet(age=25,name="Alice")
#vd3,
def molify_list(lst):
    lst.append(4)
my_list = [1,2,3]
molify_list(my_list)
print(my_list)
