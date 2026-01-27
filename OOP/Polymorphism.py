# Drill 1: The "Unified Shape" Loop

class Circle:
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        return f"{3.14*self.radius*self.radius}"


class Square:
    def __init__(self, side):
        self.side=side
    
    def area(self):
        return f"{self.side*self.side}"


c=Circle(2)
s=Square(3)

my_list=[c,s]
for x in (my_list):
    print(x.area())


print("\n")


# Drill 2: The "Animal Sounds" (Polymorphism with Functions)

class Dog:
    def speak(self):
        return f"Woof!"


class Cat:
    def speak(self):
        return f"Meow!"

def make_it_talk(animal):
    print(animal.speak())


dog=Dog()
cat=Cat()

make_it_talk(dog)
make_it_talk(cat)


print("\n")


# Drill 3: The "Payment Processor" (Polymorphism + Inheritance)

class Payment:
    def process(self, amount):
        return f"Processing generic payment of ${amount}"

class Creditcard(Payment):
    def process(self, amount):
        total=amount +(amount*0.03)
        return f"Credit Card: Paid ${total} (includes 3% fee)"

class PayPal(Payment):
    def process(self, amount):
        total=amount+5
        return f"PayPal: Paid ${total} (includes $5 fee)"


cc=Creditcard()
pp=PayPal()
payments=[cc,pp]

for x in payments:
    print(x.process(100))


print("\n")


# Drill 4: The "Vehicle Speed" (Polymorphism)

class Car:
    def __init__(self, distance, time):
        self.distance=distance
        self.time=time
    
    def get_speed(self):
        return f"Speed: {self.distance / self.time}"


class Runner:
    def __init__(self,steps_per_minute, stride_length):
        self.steps_per_minute=steps_per_minute
        self.stride_length=stride_length
    
    def get_speed(self):
        return f"Speed: {(self.steps_per_minute * self.stride_length)/60}"


c1 = Car(100, 2)
r1 = Runner(180, 1.2)

my_list=[c1, r1]

for x in my_list:
    print(x.get_speed())


print("\n")


# Drill 5: The "Grand Finale" (Method Overloading Simulation)

class Calculator:
    def add(self, a, b=0, c=0):
        return f"Result: {a+b+c}"

calc=Calculator()

print("Adding one number:")
print(calc.add(5))

print("\n")

print("Adding two number:")
print(calc.add(5,10))

print("\n")

print("Adding three number:")
print(calc.add(5,10,15))
