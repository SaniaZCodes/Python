first_name= input("Enter first name: ")
last_name=input("Enter last name: ")
birth_year=input("Enter birth year: ")
c="@company.com"

# email generation
email= (last_name[0:4]+first_name).lower()+c

# password generation
password=first_name[:2]+birth_year[-2:]+last_name[-3:]

print("\nEmployee Credentials")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Birth Year: {birth_year}")
print(f"Email Id: {email}")
print(f"Password: {password}")
