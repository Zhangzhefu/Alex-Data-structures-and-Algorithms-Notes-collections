# Python's split() method by default uses whitespaces (spaces, tabs, newlines, etc.) as the delimiter,
# so if the .split() is called without parameters, it will automatically split the string at each white space:

input_string = "4 5 6 7 8"
input_list = input_string.split()

print(input_list)  # Output would be: ['4', '5', '6', '7', '8']
