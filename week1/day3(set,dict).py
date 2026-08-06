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


#dictionary is a collection which is ordered, changeable and does not allow duplicates.
student = {
    "name": "Ram",
    "age": 20,
    "course": "BIT"
}
print(student)

#q1 accessing, updating and adding new key-value pairs in a dictionary
student = {
    "name": "Sita",
    "age": 19
}

# Access
print(student["name"])
# Update
student["age"] = 20
# Add new key
student["course"] = "BCA"
print(student)

#Q2 iterate through a dictionary
student = {
    "name": "Ram",
    "age": 20
}

for key, value in student.items():
    print(key, ":", value)


#nested dictionary
students = {
    "Ram": {"Math": 80, "Science": 75},
    "Sita": {"Math": 90, "Science": 95},
    "Hari": {"Math": 85, "Science": 80}
}

highest_student = ""
highest_total = 0

for student, subjects in students.items():
    total = sum(subjects.values())

    if total > highest_total:
        highest_total = total
        highest_student = student

print(highest_student, highest_total)

#q3 find the key with the highest value in a dictionary
marks = {
    "Ram": 85,
    "Sita": 92,
    "Hari": 78,
    "Gita": 95
}

highest = max(marks, key=marks.get)

print("Highest scorer:", highest)
print("Marks:", marks[highest])

#Q4 remove duplicates from a dictionary based on values
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

result = {}

for key, value in data.items():
    if value not in result.values():
        result[key] = value

print(result)

#q5 count each character in a string and store the result in a dictionary
text = "programming"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)




#file handling
with open("week1/sample.txt", "r") as file:
    words = file.read().lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

most_word = ""
highest = 0

for word, count in frequency.items():
    if count > highest:
        highest = count
        most_word = word

print("Most frequent word:", most_word)
print("Frequency:", highest)



