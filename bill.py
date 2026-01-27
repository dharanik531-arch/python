# bill generator

product=["rice","shompoo","bread","shoew","bat","oil"]

print (product)

product_name=input("enter the pro name :")
quantity=int(input("enter the quantity :"))

discount=0
price=0

if   product_name=="rice":
    discount=10
    price=60
elif product_name=="shampoo": 
    discount=2
    price=24
elif product_name=="bread":
    discount=10
    pice=30
elif product_name=="shoew":
    discount=20
    price=250
elif product_name=="bat":
    discount=50
    price=3000
elif product_name=="oil":
    discount=29
    price=150

else :
     discount=0
     price=0

print("""------------------------------------
$ Relaince $
------------------------------------""")

print("product_name :",product_name )
print("quantity :",quantity)
print("price",price)
print("discount",discount)


total_amount=quantity*price
discount_amount=(total_amount/100)*discount
total=total_amount-discount_amount

print("""---------------------------------""")
print("total to pay :",total)
print("""---------------------------------""")


     
