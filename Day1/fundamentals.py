# # Strings(Are immutable in that they cannot be altered as tuples cannot)
# #String formatting: You can use both concatenation or format
# height1 = 78
# age10 = 17
# grade_of_study = "grade4"

# print("My younger sibling is " + str(height1) + " centimeters tall, " + str(17) + " years old and is in " + (grade_of_study) + " of his study")
# print(f"My younger sibling is {height1} centimeters tall, {age10} years old and is in {grade_of_study} of his study")

#Iteration though a string
letter_count = 0
string1 = "Hello Brian"
for letters in string1:
    if(letters == "l"):
        letter_count += 1
print(f"There are {letter_count} 'l' in the string")

#Enumerate function(iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of each item in the sequence)
mystr = "Technical University of Kenya"
string2 = list(enumerate(mystr))
print(string2)

kit = ['bandages','gloves','painkillers','elastoplast']
for index,kits in enumerate(kit):
    print(index,kits)

#Hex representation in string formatting
print("ABC written in (hex) \x41\x42\x43")


# Numbers(Integers and floats)
# Booleans
# String Formatting
# Everything is data
# Data types
# Lists and Tuples
# Dictionaries