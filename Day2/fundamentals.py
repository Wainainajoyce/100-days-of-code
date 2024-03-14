# Numbers(Integers, floats and complex)
value1 = 89.98
print(type(value1))
print(isinstance(value1,int)) # Checks whether the value is of mentioned datatype
print(isinstance(value1,float))
print(0b00010) #Convert binary to decimal
print(0xAC) #Convert hex to decimal
print(0o76) #Convert octal to decimal

# Booleans
#Is of two values(True,False)
print(bool(0)) #Falseness.Integer 0 has real positive or negative value hence false
print(bool('0')) # True.String 0 has a character hence true
print(bool('')) #An empty string has no value hence false


# Dealing with the floating point math
add0 = 0.2 + 0.1
print(add0)
from decimal import Decimal as D
add1 = D('0.2') + D('0.1')
print(add1)

# The Fraction function
from fractions import Fraction as F
print(F(1.5))
print(F(1,5))


#The math module
import math
print(math.pi)
print(math.cos(10))
print(math.tan(10))
print(math.exp(10))

# The random module
import random
print("Random number 1 is: ", random.randrange(20,100))
print("Random number 2 is: ", random.randrange(20,100))
print("Random number 3 is: ", random.randrange(20,100))
print("Random number 4 is: ", random.randrange(20,100))

# Random choice
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print(random.choice(days))
# Random shuffle
random.shuffle(days)
print(days)

# Random element
print(random.random())


