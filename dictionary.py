#dictionary

user={"name": 'dharani', "age":22,"area": 'salem'}

print(user)

print (user["age"])

print(user.get("age"))

for i in user :

    print(i, ":", (i))

#update

user ["area"]='5 roads'

print (user)

print (user.keys())

print(user.values())

print (user.items())

user.update({"name": "dharanidharan"})

print (user)

user.update({"age":20})



print (user)

for i in user:

     print (i,":", (i))
