#Access and modify the private variable using getter and setter methods
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def credit(self, amount):
        self.__balance += amount

    def debit(self, amount):
        self.__balance -= amount

    def display_balance(self):
        print(f"Current balance: {self.__balance}")
bank = Bank(1000)
bank.display_balance()  
bank.credit(500)
bank.display_balance()  
bank.debit(200)
bank.display_balance() 
'''
 Inheritance : Acquiring properties from one class to another class is called inheritance. 
 
 Types of inheritance:
 1. Single Inheritance: A child class inherits from a single parent class.
 2. Multiple Inheritance: A child class inherits from multiple parent classes.  
 3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
 4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
 5. Hybrid Inheritance: A combination of two or more types of inheritance.
'''
#Single Inheritance
class Parent:
    def parent_method(self):
        print("This is a method from the Parent class.")

class Child(Parent):
    def child_method(self):
        print("This is a method from the Child class.")


child = Child()
child.parent_method()  
child.child_method()  

#Multi level Inheritance
class Grandparent:
    def grandparent_method(self):
        print("This is a method from the Grandparent class.")
        
class Parent(Grandparent):
    def parent_method(self):
        print("This is a method from the Parent class.")

class Child(Parent):
    def child_method(self):
        print("This is a method from the Child class.")


child = Child()
child.grandparent_method()  

child.parent_method()       
child.child_method()        


