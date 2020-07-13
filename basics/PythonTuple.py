my_tuple = ("apples","oranges","grapes")
print(my_tuple)
print(my_tuple[1])
# -1 index will access the last element from the tuple
print(my_tuple[-1])

print(my_tuple[0:3])
print(my_tuple[0:2])

for val in my_tuple:
    print(val)

# my_tuple[3] = "cherry"   this is not allowed
# del my_tuple[2] not possible

# del my_tuple  possible

print(len(my_tuple))

my_tuple2 = ("Banana",(1,2,3),["Berlin","Delhi"])
print(my_tuple2)
print(my_tuple2[2][1])

my_tuple2[2][1] = "London"
print(my_tuple2)

# to check if a particular element is there or not
print("Banana" in my_tuple2)  # True
print("cherry" in my_tuple2)  # False

