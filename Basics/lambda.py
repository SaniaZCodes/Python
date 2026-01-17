# Drill 1: The "Quick Calculator" (Basics)
#  Goal: Convert a standard function into a lambda. 

def square(x): 
    return x * x

quick_square= lambda x:x*x

multiply=lambda x,y:x*y

print(square(4))
print(quick_square(3))
print(multiply(7,2))


print("\n")


# Drill 2: The "List Purifier" (Lambda with filter)
# Goal: Use lambda inside a filter() function.

ages = [12, 18, 25, 10, 30, 15, 45, 17]
adults=list(filter(lambda x: x>=18, ages))
print(adults)


print("\n")


# Drill 3: The "Data Transformer" (Lambda with map)
# Goal: Use lambda inside a map() function.

prices = [100, 250, 400, 500]
discounted_prices=list(map(lambda x:x*0.9, prices))
print("Original Prices: ",prices)
print("Discounted Prices: ",discounted_prices)
