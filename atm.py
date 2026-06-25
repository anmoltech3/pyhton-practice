def atm():
    balance = 25000
    pin = "2006"
    p = input("enter pin: ")
    if p == pin:
        operation = input("enter operation (balance/deposit/withdraw): ")
        if operation == "balance":
            print("balance:", balance)

        elif operation == "deposit":
         amount = int(input("enter amount: "))
         balance += amount
         print("balance:", balance)

        elif operation == "withdraw":
            amount = int(input("enter amount: "))

            if amount <= balance:
                balance = amount
                print("take your cash")
                print("balance:", balance)
            else:
                print("low balance")

        else:
           print("invalid operation")
        
    else:
        print("wrong pin")

atm()
           
    