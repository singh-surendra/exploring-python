print("hello world and suri")

# variables are case-sensitive, letters (a-z), underscore, numbers(0-9)
x = 5
y = "automation"
print(x)
print(y)

print("hello " + y)

# Existing variable values can be changed
x= 5
y = 10
print(x+y)

#syntax: identation is important, write block and then:, press enter

if 10 > 5:
    print("10 is greater than 5")

# functions :

def sum(a,b):
    print(a+b)

x = sum(40,10)

# comment: select the line of codes for comment and press Cmd+/

# Numbers

x = 10
y = 2.5
z= 4j
print(type(x))
print(type(y))
print(type(z))


# Casting
x = int(2)    # 2
y = int(2.5)    # 2
z = float(1)    # 1.0
p = str(10)    # "10"
print(x)
print(y)
print(z)
print(p)

# Strings, index starts with 0

x = "hello,world..  "
print(x)
print(x[1])
print(x[6:11])
print(len(x))
print(x.lower())
print(x.upper())
# Strings, remove all white spaces in start and end
print(x.strip())
print(x.replace("e","a"))
print(x.split(","))

# Input from user
print("enter your name..")
x = input()
print("hello, " + x)









