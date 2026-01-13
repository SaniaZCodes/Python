#The "Skip & Stop" Logic
# Goal: Use range(), continue,  break

for x in range(1, 20, 1):
    if x==15 :break
    if (x%3==0):
        continue
    print(x)
    

# The "Natural Sum" with Else
# Goal: Calculate a sum and use the else keyword

N=int(input("\nEnter any number: "))
sum=0
for x in range(1,N+1):
    sum=sum+x
else:
    print("Calculation successfully finished for ",N," numbers!")

print("Result: ",sum)


print("\n")

# The "Skeleton" Loop (Pass Keyword)
# Goal: Understand how to leave "placeholders" in code.

colors=["red","blue","green","yellow","black"]
for x in colors:
    if x=="green":
        pass
    else:
        print("Checking: ",x)
