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






    
