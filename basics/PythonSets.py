my_set = {"Chalk","Duster", "Board"}
print(my_set)

for x in my_set:
    print(x)
# to check if a particular element is there or not
print("Chalk" in my_set)

# adding single element
my_set.add("Pen")
print(my_set)

# adding multiple  elements in one go
my_set.update(["Pencil","Eraser"])
print(my_set)

print(len(my_set))

my_set.remove("Pencil")
print(my_set)
my_set.discard("Pen")
print(my_set)

# my_set.remove("Pencil")
my_set.discard("Pen")

my_set.pop()
my_set.clear()
print(my_set)

del my_set

my_set2 = {"Apples",1,2,(3,4,5)}
print(my_set2)

# to convert a list into set
my_list = [1,2,3]
print(my_list)
my_set3 = set(my_list)
print(my_set3)

# UNION , INTERSECTION, DIFF, SYMMETRIC DIFF

A = {'A', 'B', 1,2,3}
B = {'B', 'C', 3,4,5}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(A.symmetric_difference(B))
print(A ^ B)








