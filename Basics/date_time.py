import datetime

# Drill 1: The "Now" Snapshot (Basics)
# Goal: Fetch current time and break it into pieces.

now= datetime.datetime.now()
print(now)
print("Year: ",now.strftime("%Y"))
print("Month: ",now.strftime("%B"))


print("\n")


# Drill 2: The "Format Master" (strftime)
# Goal: Convert a date object into a "human-readable" string.

print("Day Name: ",now.strftime("%A"))
print("Date: ", now.strftime("%d/%m/%Y"))


print("\n")


# Drill 3: The "Future Planner"
# Goal: Create a specific date manually.

past_date = datetime.datetime(1947, 8, 14)
print("Independence Day: ",past_date)
print(past_date.strftime("%A"))
