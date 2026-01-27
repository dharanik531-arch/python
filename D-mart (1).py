Product=["Rice","Shampoo","Bisciut","Egg","Bat"]
print(Product)
product_name=input("Enter the product :")
quantity=int(input("Enter the quantity :"))
discount=0
price=0
if product_name=="Rice":
    discount=10
    price=60
elif product_name=="Shampoo":
    discount=15
    price=120
elif product_name=="Bisciut":
    discount=5
    price=20
elif product_name=="Egg":
    discount=2
    price=7.5
else:
    discount=0
    price=0
print("""----------------------------------------------
                  🛒 D-Mart 🛍️
-----------------------------------------------""")
print("Product Name :",product_name)
print("Quantity     :",quantity)
print("Price        :",price)
print("Discount     :",discount,"%")
totalamount=quantity*price
discountamount=(totalamount/100)*discount
total=totalamount-discountamount
print("-----------------------------------------------")
print("Total to Pay :",total)
print("-----------------------------------------------")
print("          🤗 Thankyou for visiting🤗")


