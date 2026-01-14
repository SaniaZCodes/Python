correct_pin="1234"
i=0
balance=1000
while(i<3):
    pin=input("Enter PIN: ")
    if correct_pin==pin:
        print("Access granted")
        print("Bank Operations")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        choice= int(input("Select your choice: "))
        match choice:
            case 1:
                amount=int(input("Enter amount: Rs."))
                balance=balance+amount
                print("Updated balance: Rs.",balance)
            case 2:
                amount=int(input("Enter amount: Rs."))
                if balance>=amount:
                    balance=balance-amount
                    print("Updated balance: Rs.",balance)
                else:
                    print("Insufficent Balance")
            case 3:
                print("Balance: Rs.",balance)
            case _:
                print("Invalid option")
        
        pending_fees=[20, 50, -10, 100, 2000, 30]
        for x in pending_fees:
            if x<0:
                continue
            if x>500:
                break
            balance-=x
        
        if balance>=0:
            print("Balance: Rs.",balance)
        
        if 2000 in pending_fees:
            print("Security Alert.")
        break
    else:
        i=i+1
        if i==3:
            print("Account Locked")
            break
