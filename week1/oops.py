#object
class Student:
    def display(self):
        print("Hello, I am a student.")

# Creating an object
s1 = Student()

# Calling the method
s1.display()


#constructor
print("\nConstructor Example:")
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("John", 20)
s2 = Student("Alice", 22)

s1.display()
print()
s2.display()

#method
print("\nMethod Example:")


class Calculator:

    def add(self, a, b):
        return a + b

calc = Calculator()

print(calc.add(10, 20))

#inheritence
pritn("\nInheritance Example:")
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.sound()
d.bark()