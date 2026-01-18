# Drill 1: The "Legacy" .format()
# Goal: Learn the older method still used in many professional codebases.

item = "Laptop" 
price = 1200
txt="The {0} costs {1} dollars"
print(txt.format(item, price))


print("\n")


# Drill 2: The "Modern" f-string
# Goal: Use the most efficient and readable way to format strings.

name = "Sania" 
score = 95
print(f"Student: {name} | Score: {score*10}%")


print("\n")


# Drill 3: Precision & Alignment
# Goal: Control how numbers look (decimal places).

pi = 3.14159265
print(f"Value of pi: {pi:.2f}")
