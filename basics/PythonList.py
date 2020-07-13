my_list = ["Berlin","London", "Delhi"]
print(my_list)
print(my_list[0])

my_list[2] = "Frankfurt"
print(my_list)

for val in my_list:
    print(val)
print(len(my_list))
my_list.append("Bosten")
print(my_list)

my_list.insert(4,"Dubai")
print(my_list)

my_list.remove("London")
print(my_list)

# pop without index will remove the last element from the list
my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

del my_list[1]
print(my_list)

my_list.clear()
print(my_list)

fruits = ["apple","orange","cherry"]
print(fruits)
fruits.reverse()
print(fruits)

# list can have multiple data types
my_list2 = ["apple",1,2,3.0]
my_list3 = ["apple",[1,2,3], ['a','b','c']]
print(my_list3)
print(my_list3[1][1])

