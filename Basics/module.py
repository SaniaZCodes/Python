import auth
from math_tools import square
import very_long_database_helper_name as db

# Drill 1: The "Split Personality" (Basic Import)
# Goal: Create a separate file for logic and call it from a main file.

auth.login("Bro")


print("\n")


# Drill 2: The "Selective Import" (from ... import)
# Goal: Import only a specific function to keep your program memory-efficient.

x=square(4)
print("Square of 4:",x)


print("\n")


# Drill 3: The "Alias" (import ... as)
# Goal: Give a module a shorter nickname to save time typing.

db.connect()
