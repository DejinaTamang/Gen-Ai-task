#Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable, and unindexed.

#Q1
fruits = {"apple", "banana", "orange", "apple"}
print(fruits)

#Q2
numbers = {1, 2, 3}
numbers.add(4)
numbers.remove(2)
numbers.discard(10)
print(numbers)

#Q3
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))

#Q4
A = {1, 2, 3}
B = {2, 3, 4}

print(A.intersection(B))


