#  Exercise - count the number of times a character appears in a string

input_string = input("Enter character: ")
to_object = {}

for i in input_string:
    if(i in to_object):
        to_object[i] += 1
    else:
        to_object[i] = 1
        
print(to_object)