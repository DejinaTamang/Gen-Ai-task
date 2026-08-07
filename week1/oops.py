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
print("\nInheritance Example:")
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()
d.sound()
d.bark()

#creat multiple obj
print("\nMultiple Objects Example:")
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)


student1 = Student("John", 20)
student2 = Student("Alice", 22)
student3 = Student("Ram", 19)

student1.display()

print()

student2.display()

print()

student3.display()


#inheritance a bit deep
print("\nInheritance Example:")
# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print("----- Person Information -----")
        print("Name :", self.name)
        print("Age  :", self.age)


# Child Class
class Student(Person):

    def __init__(self, name, age, roll_no, course):
        # Call the parent class constructor
        super().__init__(name, age)

        # Child class attributes
        self.roll_no = roll_no
        self.course = course

    def show_student_info(self):
        # Parent method
        self.show_person_info()

        # Child attributes
        print("Roll No :", self.roll_no)
        print("Course  :", self.course)

    def study(self):
        print(self.name, "is studying", self.course)


# Create Object
student1 = Student("John", 20, 101, "BIT")

# Call Methods
student1.show_student_info()

print()

student1.study()

#polymorphism
print("\nPolymorphism Example:")
class Car:

    def move(self):
        print("The car is driving on the road.")


class Airplane:

    def move(self):
        print("The airplane is flying in the sky.")


class Boat:

    def move(self):
        print("The boat is sailing on the water.")


def start(vehicle):
    vehicle.move()


car = Car()
plane = Airplane()
boat = Boat()

start(car)
start(plane)
start(boat)

#encapsulation
print("\nEncapsulation Example:")
class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):

        self.__balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount
            print(f"Withdrawn {amount}")

        else:

            print("Insufficient Balance")

    def check_balance(self):

        print("Current Balance:", self.__balance)


account = BankAccount("John", 5000)

account.check_balance()

account.deposit(1000)

account.withdraw(2000)

account.check_balance()

print(account.owner)

# print(account.__balance)

#abstract class
print("\nAbstract Class Example:")
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):

        self.length = length
        self.width = width

    def area(self):

        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return 3.14 * self.radius * self.radius


r = Rectangle(10, 5)

print("Rectangle Area:", r.area())

c = Circle(7)

print("Circle Area:", c.area())