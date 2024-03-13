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
# The list converts the string into a list
string2 = list(enumerate(mystr))
print(string2)

kit = ['bandages','gloves','painkillers','elastoplast']
for index,kits in enumerate(kit):
    print(index,kits)

#Hex representation in string formatting
print("ABC written in (hex) \x41\x42\x43")


name = "Mary"
grade = 5
gender = "female"
height = 10
math_test = 70.7688

#Using argument specifiers
print("%s is a grade %d student. Mary is a %s and has a height of %d centimeters.She achieved %.2f in Maths test" % (name,grade,gender,height,math_test))

#Using format function with positional specifiers
print("{0} is a grade {1} student. Mary is a {2} and has a height of {3} centimeters.She achieved {4} in Maths test".format(name,grade,gender,height,math_test))

# Using format implicit order
print("{} is a grade {} student. Mary is a {} and has a height of {} centimeters.She achieved {} in Maths test".format(name,grade,gender,height,math_test))

#Using format with keyword argument
print("{first} is a grade {second} student. Mary is a {third} and has a height of {fourth} centimeters.She achieved {test} in Maths test".format(first = name,second = grade,third = gender,fourth = height,test = math_test))


#Using string functions
string3 = "toDay Is oN a MoNDay"
string4 = string3.lower()
string5 = string3.upper()
string6 = string3.capitalize()
string7 = string3.replace("Is","during")
print(string3)
print(string4)
print(string5)
print(string6)
print(string7)

# Formatting a long number with commas
print('{:,}'.format(72927830863736))

