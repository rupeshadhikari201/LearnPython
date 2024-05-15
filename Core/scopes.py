a = 50
b = 100

def func():
    a = 20
    global b
    print(a + b)

func()
print("the dict of all global variables : ", globals().items())