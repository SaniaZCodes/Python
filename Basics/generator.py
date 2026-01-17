# Drill 1: The "Lazy Counter" (Basics)
# Goal: Create a simple generator and understand how to retrieve values.

def count_up_to(n):
    i=1
    while i<=n:
        yield i
        i=i+1

counter = count_up_to(3)
print(next(counter))
print(next(counter))
print(next(counter))


print("\n")


# Drill 2: The "Infinite Stream" (Memory Efficiency)
# Goal: Create a generator that could theoretically run forever without crashing your RAM.

def even_numbers():
    n=0
    while True:
        yield n
        n=n+2

print("The first 10 even numbers: ")
count =0
for x in even_numbers():
    print(x)
    count=count+1
    
    if count==10:
        break


print("\n")


# Drill 3: The "Generator Expression" (The Lambda of Generators)
# Goal: Use shorthand syntax to create a generator without a def block.

numbers = [1, 2, 3, 4, 5]

gen_exp=(x*x for x in numbers)
print(gen_exp)
print(list(gen_exp))
