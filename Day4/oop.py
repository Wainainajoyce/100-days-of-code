# A function enables code reuse to perform particular actions
# A method does the same but in a class

# Object oriented programming enables creation of objects through instantiation. A class is a blueprint of an object.

class Item:

    def calculate_total_price(self,x,y):
        return x * y
        
item1 = Item()
item1.name = "phone"
item1.price = 70
item1.quantity = 5
print(item1.calculate_total_price(item1.quantity,item1.price))

