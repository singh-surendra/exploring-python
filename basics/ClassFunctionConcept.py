class MyClass:
    name = "suri"

    def __init__(self, name, age):
        self.name = name
        self.age = age



    def sum(self,a,b):
        print(a+b)



x = MyClass("John", 28)
print(x.name)
del x.name
print(x.age)
x.sum(4,5)