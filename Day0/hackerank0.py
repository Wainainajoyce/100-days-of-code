# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# You are given an immutable string, and you want to make changes to it.
# One solution is to convert the string to a list and then change the value.

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
#This line joins the modified list back into a string. It uses the join() method of strings, which concatenates each element of the list together, using an empty string as the separator. 
    string = ''.join(l)
    return string


string1 = mutate_string("Formatting",4,"i")
print(string1)



# Another approach is to slice the string and join it back.

string = ""

def mutate_string(string,position,position1,character):
    string = string[:position] + str(character) + string[position1:]
    return string

string2 = mutate_string("abracadabra",5, 6,"o")
print(string2)