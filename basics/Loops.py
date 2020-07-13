if 5 > 3:
    print("5 is greater than 3")

num = 0
if num > 0:
    print("this is positive number")
elif num == 0:
    print("num is 0")
else:
    print("this is negative number")

# List
num = [1,2,3,4,5]
for val in num:
    print(val)
sum = 0
for val in num:
    sum = sum + val
print("total is",sum)

fruits = ["apple", "grapes", "orange"]
for val in fruits:
    print(val)
else:
    print("no fruits left")

print("enter a number :")
num = int(input())
sum = 0
i = 1
while i < num:
    sum = sum + i
    i = i +1
print("total is", sum)

