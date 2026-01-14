# The "HTTP Status" Checker
# Goal: Use match to handle different server response codes.

status_code=int(input("Enter status code: "))
match status_code:
    case 200:
        print("Success")
    case 404: 
        print ("Not Found") 
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status Code")

    
print("\n")


# The "Weekend vs. Weekday" (Combined Cases)
# Goal: Use the "Pipe" operator (|) to group multiple cases together.

day=input("Enter day of week: ")
day=day.lower()
match day:
    case "saturday" | "sunday":
        print("It's the weekend!")
    case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
        print("Back to work!")
    case _:
        print("That's not a real day.")


print("\n")


# The "Role-Based Access"
# Goal: Use a variable inside the match logic.

user_role = "admin"
is_authenticated=True
match user_role:
    case "admin" if is_authenticated:
        print("Full System Access")
    case "admin" if not is_authenticated:
        print("Can not Full System Access")
    case "editor":
        print("Can edit posts only")
    case "guest":
        print("View only access")
    case _:
        print("Outsider")
