# Tuple is a collection which is ordered and unchangeable. Allows duplicate members
#q1 
# Create a tuple and access its elements using indexing and slicing.
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])

#Q2 create a tuple of fruits and print the first three fruits, last two fruits, and every second fruit using slicing.
fruits = ("apple", "banana", "mango","banana", "orange", "grapes", "kiwi")
print("First three fruits:", fruits[:3])
print("Last two fruits:", fruits[-2:])
print("Every second fruit:", fruits[::2])#start,stop,step=2

#Q3 counting the number of appereance
numbers = (5, 10, 15, 10, 20, 10,10,10, 25, 30)

# Count how many times 10 appears
count_10 = numbers.count(10)
print("10 appears", count_10, "times")

# Find the index of 20
index_20 = numbers.index(20)
print("Index of 20:", index_20)

#Q4 convert tuple to list, add a new element to the list, and then convert it back to a tuple.

colors = ("red", "green", "blue")

# Convert tuple to list
color_list = list(colors)

color_list.append("yellow")

# Convert back to tuple
colors = tuple(color_list)

# Print updated tuple
print("Updated tuple:", colors)

#Q5
student = ("Smaran", 21, "Computer Science")

# Unpack the tuple
name, age, course = student

# Print each variable
print("Name:", name)
print("Age:", age)
print("Course:", course)

# Print a sentence
print(name, "is", age, "years old and studies", course + ".")

#Q6 
tuple=("cat", "dog", "bird", "fish", "hamster")
i=0
while i<len(tuple):
    print(tuple[i])
    i+=1 

#loop
# Question 1:
# Write a program to ask the user for a number and print its multiplication table up to 10.

number = int(input("Enter a number for multiplication table: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Question 2:
# Write a program to find the sum of numbers from 1 to n.

n = int(input("Enter a number for sum calculation: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)


# Question 3:
# Write a function to calculate the factorial of a number.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

number = int(input("Enter a number for a factorial calculation: "))

print("Factorial =", factorial(number))

# Question 4:
# Write a function to find the largest of three numbers.

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Largest number =", largest(num1, num2, num3))

#loop with break
for i in range(1, 11):
    if i == 5:
        break
    print(i)

#with continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#while loop
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1

# Question 5:
# Write a program to reverse a string using a loop.

text = input("Enter a word: ")

reverse = ""

for letter in text:
    reverse = letter + reverse

print("Reversed word =", reverse)


# Question 6:
# Write a program to check whether a number is prime.

number = int(input("Enter a number for prime check: "))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

if count == 2:
    print(number, "is a Prime Number")
else:
    print(number, "is Not a Prime Number")

# Question7 :
# Write a program to count the vowels and consonants in a word.

word = input("Enter a word: ").lower()

vowels = 0
consonants = 0

for letter in word:
    if letter.isalpha():
        if letter in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)    