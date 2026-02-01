import re

# Drill 1: The "Finder" (Search for a Word)

sentence= "Python is awesome, I love Python!"
match=re.search("awesome",sentence)

if match:
    print("Found it!")
else:
    print("Not Found")


print("\n")


# Drill 2: The "Collector" (findall)

finding=re.findall("Python",sentence)
print(finding)
print("Number of times: ",len(finding))


print("\n")


# Drill 3: The "Digit Hunter" (\d)

text= "My order number is 402 and the price is 95 dollars."
matching=re.findall(r"\d",text)
for x in matching:
    print(x)


print("\n")


# Drill 4: The "Number Grouper" (\d+)

new_matching=re.findall(r"\d+",text)

class NumberTotalizer:
    def __init__(self, num_list):
        self.num_list=num_list
    
    def get_sum(self):
        total=0
        for num in self.num_list:
            total=total+int(num)
        return total

totalizer=NumberTotalizer(new_matching)
print(f"Numbers extracted: {new_matching}")
print(f"The sum is: {totalizer.get_sum()}")


print("\n")


# Drill 5: The "Grand Task" (The Data Cleaner)

Text= "The CEO of Apple and Microsoft met in London."
matches=re.findall(r"[A-Z][a-z]+", Text)

class WordProcessor:
    def __init__(self, word_list):
        self.word_list=word_list
    
    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        if self.index<len(self.word_list):
            current=self.word_list[self.index]
            self.index+=1
            return current
        else:
            raise StopIteration
    
    def make_bold(self, word):
        return f"**{word}**"

o=WordProcessor(matches)
for i in o:
    print(o.make_bold(i))
