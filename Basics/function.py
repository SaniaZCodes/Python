# Drill 1: The "Flexible Chef" (Arguments & Parameters)
# Goal: Use Positional-only, Keyword-only, and Combined arguments.

def make_pizza(size,/, *toppings, crust="Thin", **details):
    print("Size: ",size)
    print("Toppings: ")
    for x in toppings:
        print(x)
    print("Crust Type: ",crust)
    for y,z in details.items():
        print(y,":",z)

make_pizza("Large", "Pepperoni", "Mushrooms", crust="Deep Dish", delivery=True)


print("\n")


# Drill 2: The "Variable War" (Scope & Non-local)
# Goal: Master global and nonlocal keywords.

total_score = 0

def outer():
    local_score=10
    def inner():
        global total_score
        total_score=5+total_score
        nonlocal local_score
        local_score=local_score+5
    inner()
    print("Local Score: ",local_score)

outer()
print("Final Total score: ",total_score)


print("\n")


# Drill 3: The "Report Generator" (*args & **kwargs)
# Goal: Handling unknown amounts of data.

def generate_report(title, *tags, **metadata):
    print(title.upper())
    print("Tags: " + ", ".join(tags))
    for y,z in metadata.items():
        print(y,": ",z)

generate_report("Annual Sales", "Finance", "2024", "Audit", Author="Zain", Status="Final")
