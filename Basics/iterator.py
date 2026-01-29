# Drill 1: The "Limited Iteration"

class Countdown:
    def __init__(self, start):
        self.start=start
    
    def __iter__(self):
        self.current=self.start
        return self
    
    def __next__(self):
        if self.current>0:
            num=self.current
            self.current-=1
            return num
        else:
            raise StopIteration

for num in Countdown(5):
    print(num)


print("\n")


# Drill 2: The "Even Stepper"

class EvenNumbers:
    def __init__(self, max):
        self.max=max
    
    def __iter__(self):
        self.n=0
        return self
    
    def __next__(self):
        if self.n<=self.max:
            num=self.n
            self.n+=2
            return num
        else:
            raise StopIteration

e=EvenNumbers(8)
for x in e:
    print(x) 


print("\n")


# Drill 3: The "Vowel Filter"

class VowelFilter:
    def __init__(self, word):
        self.word=word
        self.vowels="aeiouAEIOU"
    
    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        while(self.index<len(self.word)):
            char=self.word[self.index]
            self.index+=1
            
            if char in self.vowels:
                return char
        
        raise StopIteration

v=VowelFilter("Python is Awsome")
for x in v:
    print(x)


print("\n")


# Drill 4: The "Power Sequence"

class PowerOfTwo:
    def __init__(self, max_exponent):
        self.max_exponent=max_exponent
    
    def __iter__(self):
        self.exp=0
        return self
    
    def __next__(self):
        if self.exp<=self.max_exponent:
            num=2**(self.exp)
            self.exp+=1

            
            return num
        
        raise StopIteration

for x in PowerOfTwo(3):
    print(x)


print("\n")


# Drill 5: The "Grand Task" (Python Word Processor)

class SentenceIterator:
    def __init__(self, sentence):
        # Splits the string into a list of words
        self.words_list = sentence.split()

    def __iter__(self):
        # Initialize the index to start at the first word
        self.index = 0
        return self

    def __next__(self):
        # Check if we still have words left in the list
        if self.index < len(self.words_list):
            current_word = self.words_list[self.index]
            self.index += 1
            return current_word
        else:
            # No more words, stop the loop
            raise StopIteration

    def format_word(self, word):
        # Python string formatting
        return f"[Word: {word}]"

# --- Testing the Word Processor ---
my_iterator = SentenceIterator("Python is powerful")

for word in my_iterator:
    print(my_iterator.format_word(word))
