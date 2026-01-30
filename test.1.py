'''1. Coffee Shop Ordering System (Basic)
Scenario:
You are developing a simple ordering system for a new coffee shop. The system needs to calculate the total bill for a customer's order and apply a discount if applicable. 
Task:
Create a Python program that performs the following actions:
Display a menu with item names and prices (e.g., Coffee: $3.50, Muffin: $2.00, Bagel: $4.00).
Prompt the user to select items and quantities.
Calculate the total cost of the order.
Apply a 10% discount if the total bill exceeds $20.00.
Display the final amount payable.'''


menu=("coffee :, muffin :,bagel :")
print(menu)
menu_order=input("Enter the order name :")
quantity=int(input("Enter the quantiy :"))
discount=0
if menu_order=="coffee" :
            price=10
elif menu_order=="muffin" :
            price=10
elif menu_order=="bagel":
             price=15
else :
    price=0
    print('''------------------------------------
xxx coffee shop
-----------------------------------''')
    

print("menu_order :",menu_order)
print("quantity:",quantity)
print("price :",price)
print("discount :",discount)
total_amount=quantity*price
print("total_amount",total_amount)
quantity=(total_amount / 100)*discount
print("price")
total=total_amount-discount
print('''--------------------------------------------''')
print(   "total pay :",total)
print('''--------------------------------------------''')


'''2.Scenario: You are processing credit card numbers (e.g., "4532111188885678").
Task: Write a function that:
Takes the string as input.
Returns a "masked" version where all digits except the last 4 are replaced by * (e.g., "************5678").
Focus: Function definitions, string slicing, and the * repetition operator.'''


def mask_creditcard(card_number):
    masked="*" *(len(card_number)-4)+card_number[-4:]
    return masked
card="11122224445555030"
print(mask_creditcard(card))




    
