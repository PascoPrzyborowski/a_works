

# from collections import namedtuple


# class Person:
#     def __init__(self,name, address):
#         self.name = name 
#         self.address = address

#     def talk_self(self):
#         return f"Hi,my name is {self.name}, I live in {self.address}"

# shaban = Person('Shaban', 'Berlin')
# names = ['shaban,'jac', 'emily']
# locations = ['Berlin','Hamburg','Munich']


class Person:

    def __init__(self, name, address): 
        self.name = name
        self.address = address
    # functions within classes are called methods.
    def talk_about_yourself(self):
        return f"Hi, my name is {self.name}. I live in {self.address}"


# instance (object)    
# instantiation ! 
shaban = Person('Shaban', 'Berlin')
names = ['shaban', 'jacques', 'peer']
locations = ['Berlin', 'Hamburg', 'Munich']

collection = []
for name, location in zip(names, locations):
    collection.append(Person(name, location))
print(collection)

talk_about_self = [instance.talk_about_yourself() for instance in collection]
print(talk_about_self)

# class Order:
#     def __init__(self,products, shipping_address, sku, billing_address,tracking_number, invoice):
#         self.products = products
#         self.shipping_address = shipping_address
#         self.sku = sku
#         self.billing_address = billing_address
#         self.invoice = invoice
#         if(billing_address != shipping_address):
#             raise Exception('Invalid billing address')

# class Payment:
#     def __init__(self,, CC,Cvv, expiration_date):
#         pass

# class chat:
#     def __init__(self, name, email, message):
#         pass

# class Student:
#     def __init__(self, name, classes, faculty):
#         self.name = name
