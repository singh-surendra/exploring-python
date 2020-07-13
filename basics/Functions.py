# def func_name(parameter):
#     body


def printHello():
    print("hello")

printHello()

# John will be default value for below function
def printHi(name="John"):
    print("Hi",name)

printHi("suri")
printHi()

def sum(a,b,c):
    print(a+b+c)
sum(10,20,30)

def returnSum(a,b):
    """this is a fucntion to calculate sum of two numbers, this is how we can have function description"""
    return a+b

x = returnSum(10,20)
print(x)

