# Drill 1: The "Simple Nest"

class Computer:
    def __init__(self, brand, cpu_model):
        self.brand=brand
        self.cpu=self.CPU(cpu_model)
    
    class CPU:
        def __init__(self, model):
            self.model=model
        
        def display(self):
            print("Model: ",self.model)

my_comp = Computer("Dell", "i7")
my_comp.cpu.display()


print("\n")


# Drill 2: The "Independent Inner" (Manual Instantiation)

class Student:
    def __init__(self, name):
        self.name=name
    
    class Laptop:
        def show_specs(self):
            print("8GB RAM, 256GB SSD")

s1= Student("Zaryab")
lap1=s1.Laptop()
lap1.show_specs()


print("\n")


# Drill 3: The "Nested Car" (Double Inner Class)

class Car:
    def __init__(self, make):
        self.make=make
    
    class Engine:
        def start(self):
            print("Vroom Vroom!")
    
    class Wheels:
        def rotate(self):
            print("Wheels are spinning...")

car=Car("Toyota")
engine=car.Engine()
engine.start()
wheels=car.Wheels()
wheels.rotate()


print("\n")


# Drill 4: The "Deep Secret" (Private Inner Class)

class Bank:
    def __init__(self):
        self.vault=self.__Security()
    
    class __Security:
        def validate(self):
            return f"Security Check Passed!"
    
    def open_vault(self):
        print(self.vault.validate())

my_bank=Bank()
my_bank.open_vault()

try:
    hack = my_bank.__Security()
except AttributeError:
    print("\nHack Failed: Cannot access private inner class '__Security'!")


print("\n")


# Drill 5: The "Grand Finale" (Multilevel Nesting)

class Universe:
    class Galaxy:
        class Planet:
            def name(self):
                print("I am Earth")

u=Universe()
g=u.Galaxy()
p=g.Planet()
p.name()
