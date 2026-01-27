print("--------------------------------------------------------------------------------")
print("                            ATM TASK ")
print("--------------------------------------------------------------------------------")

pin = int(input("Enter pin  : "))
correct_pin = 1234
balance = 10000

if pin == correct_pin:
    choice = input("withdraw / deposit : ")
    amount = int(input("Enter Amount : "))

    if choice == "withdraw":
        if amount <= balance:
            withdraw=amount
            print("Transaction Successful")
            withdraw_amt = withdraw
            balance=balance-withdraw
            deposit_amt = 0
        else:
            print("Insufficient amount")

    elif choice == "deposit":
        deposit=amount
        print("Transaction Successful")
        balance= balance+amount
        deposit_amt = deposit
        withdraw_amt = 0

    else:
        print("Invalid choice")
        deposit_amt = 0
        withdraw_amt = 0

    receipt = input("If you want receipt (yes / no) : ")

    if receipt == "yes":
       print("--------------------------------------------------------------------------------")
       print("                            XYZ BANK")
       print("--------------------------------------------------------------------------------")
       print("Account number       : 023658516")
       print("Account Holder Name  : XXXXXX")
       print("Deposited amount     :", deposit_amt)
       print("Withdraw amount      :", withdraw_amt)
       print("Balance              :", balance)
       print("--------------------------------------------------------------------------------")
       print("                      😊 Thank you for visiting 😊")
       print("--------------------------------------------------------------------------------")

    else:
        print("--------------------------------------------------------------------------------")
        print("😊 Thank you for visiting 😊")

else:
    print("Invalid PIN")
