import time

# Drill 1: The "Logging Box" (Basic Decorator)
# Goal: Create a decorator that prints a message before and after a function runs.

def log_decorator(fun):
    def wrapper():
        print("System: Starting function...")
        fun()
        print("System: Function finished.")
    return wrapper

@log_decorator
def say_hello():
    print('Hello from Original Function')

say_hello()


print("\n")


# Drill 2: The "Safety Lock" (Decorators with Arguments)
# Goal: Use a decorator to check the inputs of a function.

def check_positive(fun):
    def wrapper(*args, **kwargs):
        all_values=list(args)+list(kwargs.values())
        for x in all_values:
            if x<=0:
                print("Error: Values must be positive!")
                break
        else:
            return fun(*args, **kwargs) 
    return wrapper

@check_positive
def calculate_area(length, width):
    return length * width

print("Result 1: ", calculate_area(3,2))
print("Result 2: ", calculate_area(-4,2))


print("\n")


# Drill 3: The "Timing Challenge" (Real-world Use Case)
# Goal: Calculate how long a function takes to run.

def time_decorator(fun):
    def wrapper():
        start=time.time()
        fun()
        end=time.time()
        print(f"Execution time: {end} - {start} seconds")
    return wrapper


@time_decorator
def long_loop():
    for x in range(1,1000000):
        print(x)

long_loop()
