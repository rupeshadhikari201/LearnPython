# Lambda Function
'''
A function without a name is called as Anonymous Function. It is also known as Lambda Function.
Anonymous Function are not defined using def keyword rather they are defined using lambda keyword.
Syntax:- lambda argument list : expression
It returns a function.
'''

exp = lambda x : x**2
num = lambda x : print(x, end=" ")
sum = lambda x,y : x+y
print("the exp func is : ", exp(3))
print("the num func is : ", num(3))
print("the num func is : ", sum(3,5))

# *Important Points about lambda Functions*
'''
    1. Lambda Function doesn't have any Name
    2. Lambda function returns a function
    3. Lambda function can take zero or any number of argument but contains only one expression
    4. It can only contain expressions and can't include statements in its body
    5. You can use all the type of Actual Arguments
'''

add_sum = lambda x,y : (x+y, x-y)
s, d = add_sum(5,3)
print("resut of add_sum function : ", s, d)


# Nested Lambda Function
sum = lambda x=10 : lambda y : (x+y)
temp = sum()
res = temp(20)
print("the outer lambda func is : ", temp)
print("the inner lambda func is : ", res)

# Lambda Function inside a Function
def show(lamfunc):
    print("lambda function inside a normal function : ",  lamfunc(10))

show(lambda x : x**2)

# Return Lambda Function from a Function
def return_lambda():
    a = 5
    return lambda x: x**a

returned_lambda_func = return_lambda()
print("the result of returned_lambda_func is : ", returned_lambda_func(2))


# Immediately Invoked Function Expression (IIFE)
iife = (lambda x : x**2)(5)
print("this is an example if IIFE : ", iife)