print("Hello World!")

# Variable with a string stored
# A string is a date type used for storing text
first_words = "Hello World!"

print(first_words)

# Here is a string with single quotes. It is still a string data type
new_string = 'I can also use single quotes'

# Escape character \
example = 'I can\'t use single quote\'s inside of single quote\'s'
print(example)

# Concatenating strings together
string1 = "This is"
string2 = 'super cool!'

concat = string1 + " " + string2 # Concatenated with a "space string" added in
print(concat)

print(string1, string2) # Concatenated with a coma , will automatically add a space between my strings.

# Docstring - a multiple string
# Incorrect format for a Docstring (a multi line string)
# another_string = "
# line1
# line2
# line3
# "

# Initiate a Docstring with triple quotes, either single '' or double ""
doc = '''
enter 1 to continue 
enter 2 to go back
enter 3 to figure it all out
'''
print(doc)

# Python reads from top down, defined variable doc, if we redefine the data stored, the our print function will print 
# that new piece
doc = "This is a new thing"
print(doc)

# Unpacking - We can define multiple pieces of data at once, and unpack them positionally into their own variable
first, middle, last = "Tyler", "Sloan", "Carlisle"
print(middle)

