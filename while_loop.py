# "Countdown & Blast Off"
# Goal: Use a while loop to count down and handle a specific condition.

timer=10
while(timer>0):
    if timer==5:
        print("Halfway there!")
    print(timer)
    timer-=1
else:
    print("Blast Off!")


print("\n")


# "Guarded Input"
# Goal: Keep asking the user for input until they give the correct answer.

secret_pin="1234"
pin=input("Enter PIN: ")
while(pin!=secret_pin):
    print("Access Denied. Try again.")
    pin=input("Enter PIN: ")
else:
    print("Access Granted!")


print("\n")


# "Infinite math" 
# Goal: Use while True (an infinite loop) and stop it using a break based on a math result.

number=1
while(True):
    number=number*2
    if number>500:
        break
    print(number)
