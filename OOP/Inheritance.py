# Drill 1: The "Multi-Level logic" (Inheritance + Logic)
# Goal: Use inheritance to create a hierarchy where the child class adds a specific logic layer to the parent's data.

class SmartDevice:
    def __init__(self, brand, status="OFF"):
        self.brand=brand
        self.status=status
    
    def report(self):
        print(f"Device: {self.brand} is currently {self.status}") 

class SmartPhone(SmartDevice):
    def __init__(self, brand,  status, battery_level ):
        super().__init__(brand, status)
        self.battery_level= battery_level
    
    def report(self):
        if (self.battery_level < 10):
            print(f"Device: {self.brand} is {self.status} - WARNING: LOW BATTERY!")
        else:
            print(f"Device: {self.brand} is currently {self.status} with {self.battery_level}%") 


phone1=SmartPhone("Nokia","On",67)
phone1.report()
print("\n")
phone2=SmartPhone("OOPO","OFF", 2)
phone2.report()


print("\n")


# Drill 2: The "Grandparent" Chain (High Difficulty)

class User:
    def __init__(self, username):
        self.username=username

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.access_level="High"

class SuperAdmin(Admin):
    def __init__(self, username, special_key):
        super().__init__(username)
        self.access_level="Supreme"
        self.special_key=special_key
    
    def show_credentials(self):
        print(f"Admin: {self.username} | Access: {self.access_level} | Key: {self.special_key}")

boss = SuperAdmin("Zaryab", "999-XYZ")
boss.show_credentials()


print("\n")


# Drill 3: The "Protected Bank" (Conditional super() Call)

class Bank:
    def __init__(self, account_type):
        self.account_type=account_type
    
    def withdraw(self , amount):
        print(f"Successfully withdrew ${amount} from {self.account_type} account.")


class SavingsAccount(Bank):
    def __init__(self):
        super().__init__(account_type="Savings")
    
    def withdraw(self, amount):
        if amount >500:
            print("Transaction Denied: Savings limit is $500!")
        else:
            super().withdraw(amount)

a1=SavingsAccount()
a1.withdraw(600)

print("\n")

a2=SavingsAccount()
a2.withdraw(300)


print("\n")


# Drill 4: The "Selective Discount" (Multiple Overrides)
# Goal: Create two different child classes that change a parent's calculation logic.

class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    
    def get_final_price(self):
        return f"Rs.{self.price}"


class DigitalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name,price)
    
    def get_final_price(self):
        return f"Rs.{self.price*0.9}"


class ImportedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name,price)
    
    def get_final_price(self):
        return f"Rs.{self.price+20}"


dg=DigitalProduct ("E-Book", 100)
print(dg.get_final_price())

imp=ImportedProduct ("iPhone", 1000)
print(imp.get_final_price())


print("\n")


# Drill 5: The "Grand Finale" (Multiple Inheritance)

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    
    def show_salary(self):
        print("Salary: Rs.",self.salary)

class Developer:
    def __init__(self, programming_language):
        self.programming_language=programming_language
    
    def show_skill(self):
        print("Programming language:",self.programming_language)


class TeamLead(Employee, Developer):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        Developer.__init__(self, programming_language)

td=TeamLead("Zaryab", 50000, "Python")
td.show_salary()
td.show_skill()
