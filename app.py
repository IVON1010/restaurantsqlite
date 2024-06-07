# ORM
"""
->class can be referenced to a whole db table
-> attributes are columns
-> a class instance can be associated with a table row
"""

#from models.menu import Menu
from models.customer import Customer
from models.inventory import Inventory

#menus = Menu.find_all(deleted=True)
#print(menus)

customer_1 = Customer("Leslie", "0712345678")
customer_1.save()
print(customer_1)

customer_2 = Customer.find_one(3)
#customer_2.save()
print(customer_2)

inventory_1 = Inventory(customer_2.id, 1000)
inventory_1.save()
inventory_2 = Inventory(customer_2.id, 400)
inventory_2.save()
