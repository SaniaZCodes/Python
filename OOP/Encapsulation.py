# Drill 1: The "Locked Vault" (Private Attributes)

class BankEmployee:
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary
    
    def show_salary(self):
        return f"Salary: {self.__salary}"
    
    def set_salary(self, new_salary):
        if new_salary>0:
            self.__salary=new_salary
        else:
            print("Error: Salary must be positive!")

emp = BankEmployee("Zaryab", 50000)
print(emp.show_salary())


print("\n")


# Drill 2: The "Safe Update" (Setters and Getters)

e2=BankEmployee("Sania",-500)
e2.set_salary(60000)
print(e2.show_salary())


print("\n")


# Drill 3: The "Family Secret" (Protected Members)

class Company:
    def __init__(self, project_name):
        self._project_name=project_name

class Department(Company):
    def show_project(self):
        print(self._project_name)


do=Department("Python OOP")
do.show_project()


print("\n")


# Drill 4: The "Internal Validation" (Private Methods)

class SmartSafe:
    def __init__(self, amount):
        self.amount=amount
    
    def __apply_tax(self, amount):
        return f"Tax: {self.amount*0.95}"
    
    def withdraw(self, amount):
        taxed_amount= self.__apply_tax(amount)
        print(f"Dispensing: ${taxed_amount} after internal tax.")


safe=SmartSafe(1000)
safe.withdraw(100) 


print("\n")


# Drill 5: The "Grand Finale" (Encapsulation + Validation)

class UserAccount:
    def __init__(self, username, password):
        self.username=username
        self.__password=password
    
    def get_password(self):
        return f"********"
    
    def set_password(self, new_password):
        if len(new_password)<6:
            print("Error: Password too weak!")
        else:
            self.__password=new_password


user= UserAccount("Sania Zafar","samo1")

print(user.get_password())

user.set_password("123")
print(user.get_password())
user.set_password("SecurePass123")
print(user.get_password())
