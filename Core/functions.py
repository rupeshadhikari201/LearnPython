# Functions and its return type
''' a function return a variable or an expression '''

def fun(x):
    return x**x
print("the result of function fun : ", fun(10))

# Nested Function

def outer():
    def inner():
        print("Hello, i'm Inner")
    inner()
    print("Hello, i'm Outer")

outer()

def out():
    def inn():
        return "Inn Called"
    temp = inn()
    return temp + " : " + "Outer Called"

print("the result of nested function is : ", out())


# Function Calling Function
def display(show):
    return "Display" + " " + show()

def show():
    return "Show"

res1 = display(show)
print("result of function calling function : " , res1)

# Function Returning Function
def display1():
    def show1():
        return "I am Show1"
    temp = "I am Display1"
    return show1 + temp
returned_function = display1()
print("the result of function returning function : ",returned_function())