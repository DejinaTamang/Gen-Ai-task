#List 
#Q1 FINDING LARGEST, SMALLEST, SUM AND AVERAGE OF NUMBERS IN A LIST
numbers = [25, 40, 15, 30, 20, 50, 10, 35]

print("Numbers:", numbers)

print("Largest Number:", max(numbers))

print("Smallest Number:", min(numbers))

print("Sum:", sum(numbers))

average = sum(numbers) / len(numbers)

print("Average:", average)

#Q2 FINDING EVEN AND ODD NUMBERS IN A LIST

numbers = [12, 5, 18, 9, 3, 20, 15, 8, 7, 10]

print("Even Numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

print("Odd Numbers:")
for num in numbers:
    if num % 2 != 0:
        print(num)

#Q3 SEARCHING NUMBERS IN A LIST0
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Numbers:", numbers)

search = int(input("Enter a number: "))

if search in numbers:
    print(search, "found at index", numbers.index(search))
else:
    print("Number not found")

#Q4 REMOVING DUPLICATES FROM A LIST
numbers = [5, 2, 7, 5, 3, 2, 9, 7, 10]

print("Original List:")
print(numbers)

new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print("\nList Without Duplicates:")
print(new_list)

#function to calculate grade based on mark
print("\nGrade Calculation:")

def calculate_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "Fail"

mark = int(input("Enter the mark: "))
grade = calculate_grade(mark)

print("Grade:", grade)




