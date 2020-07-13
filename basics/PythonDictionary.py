my_dict = {
    "class": "animal",
    "name" : "dog",
    "age" : 12
}

print(my_dict)
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.values())

# to print all the keys
for x in my_dict:
    print(x)
# to print all the keys
for x in my_dict:
    print(my_dict[x])
# to print both keys and values
for x,y in my_dict.items():
    print(x,y)

my_dict["name"] = "cat"
print(my_dict)

my_dict["color"] = "black"
print(my_dict)

my_dict.pop("color")
print(my_dict)
# to remove the last item from dictionary
my_dict.popitem()
print(my_dict)

del my_dict["class"]
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict