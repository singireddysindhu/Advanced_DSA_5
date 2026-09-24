# Revision of Object-Oriented Programming Concepts
#Apply all the 5 types of polymorphism in the below code
#Inheritance 
# 1. SINGLE INHERITANCE
class Animal:
    def eat(self):
        print("Animal eats food")


class Dog(Animal):
    def bark(self):
        print("Dog barks")



d = Dog()
d.eat()
d.bark()


# 2. MULTIPLE INHERITANCE
class Father:
    def driving(self):
        print("Father knows driving")


class Mother:
    def cooking(self):
        print("Mother knows cooking")


class Child(Father, Mother):
    def painting(self):
        print("Child knows painting")



c = Child()
c.driving()
c.cooking()
c.painting()


# 3. MULTILEVEL INHERITANCE
class Grandfather:
    def land(self):
        print("Grandfather owns land")


class Father2(Grandfather):
    def house(self):
        print("Father owns a house")


class Son(Father2):
    def bike(self):
        print("Son owns a bike")



s = Son()
s.land()
s.house()
s.bike()


# 4. HIERARCHICAL INHERITANCE
class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")



car = Car()
car.start()
car.drive()

bike = Bike()
bike.start()
bike.ride()


# 5. HYBRID INHERITANCE
class Person:
    def show_person(self):
        print("I am a person")


class Student(Person):
    def show_student(self):
        print("I am a student")


class Teacher(Person):
    def show_teacher(self):
        print("I am a teacher")


class TeachingAssistant(Student, Teacher):
    def show_role(self):
        print("I am a teaching assistant")


ta = TeachingAssistant()
ta.show_person()
ta.show_student()
ta.show_teacher()
ta.show_role()
# polymorphism
# 1. Compile-time polymorphism (Method Overloading)
def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c
# 2. Run-time polymorphism (Method Overriding)
class Shape:
    def area(self):
        pass
    
