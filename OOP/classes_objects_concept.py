# Drill 1: The "Blueprint" (__init__ and self)
# Goal: Use the constructor to initialize data when an object is created.

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

car1=Car("Tesla","Model 3")
car2=Car("Toyota","Camry")
print("Car1 Brand: ",car1.brand)
print("Car2 Model: ",car2.model)


print("\n")


# Drill 2: The "Behavior" (Object Methods)
# Goal: Add functions inside the class that use the object's data.

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def result(self):
        if self.marks>50:
            print("Pass")
        else:
            print("Fail")

s1=Student("Sania",85)
s1.result()


print("\n")


# Drill 3: The "Representation" (__str__ Method)
# Goal: Control what happens when you print(object).

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

my_book=Book("Atomic Habits","James Clear")
print(my_book)
