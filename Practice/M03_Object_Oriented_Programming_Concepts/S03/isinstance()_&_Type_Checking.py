'''
#isinstance : The isinstance() function checks whether a value belongs to a particular data type.
a=10
b="Hello"
c={"name":"John", "age":30}
print(isinstance(a,int))
print(isinstance(a,str))
print(isinstance(b,float))
print(isinstance(c,dict))
#multiple values
x=10
if isinstance(x,(float,str)):
    print("x is a number")
else:
    print("x is not a number")
#checking with classes:'
class a:
    def show(self):
        print("a")
class b(a):
    pass
c=b()
c.show()
print(isinstance(c,b))
print(isinstance(c,a))

#Typechecking : The type() function returns the data type of a value.
a=10
b=[1,2,3,4,5,12.3]
c={1,2,3}
print(type(a))
print(type(b))
print(type(c))
'''
#Duck typing: same method acts as same behaviour for different data types
class Dog:
    def sound(self):
        return "Woof!"  

class Cat:
    def sound(self):
        return "Meow!"
def animal_sound(animal):
    print(animal.sound())
d=Dog()
c=Cat()
animal_sound(d)
animal_sound(c)
#example of duck typing with different data types
def process(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper() 
    elif isinstance(data, float):
        return data * 10.5
print(process(5))
print(process("hello"))
print(process(3.14))
#Interview question
class A:
    pass
class B(A):
    pass
obj=B()
print(type(obj)==B)
print(type(obj)==A)

print(isinstance(obj,B))
print(isinstance(obj,A))