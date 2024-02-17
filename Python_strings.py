'''Python Strings'''
'''
A String is a data structure in Python that represents a sequence of characters. 
It is an immutable data type, meaning that once you have created a string, you cannot change it. 
Strings are used widely in many different applications, such as storing and manipulating text data, 
representing names, addresses, and other types of data that can be represented as text.
Python does not have a character data type, a single character is simply a string with a length of 1.
'''


#Creating a String in Python
'''
Strings in Python can be created using single quotes or double quotes or even triple quotes. 
Let us see how we can define a string in Python.
'''

#Example:
'''
In this example, we will demonstrate different ways to create a Python String. 
We will create a string using single quotes (‘ ‘), double quotes (” “), and triple double quotes (“”” “””). 
The triple quotes can be used to declare multiline strings in Python.
'''

String1 = 'Welcome to the Python Learning'
print("String with the use of Single Quotes: ", String1)

# Creating a String
# with double Quotes
String1 = "I'm Learning Python"
print("String with the use of Double Quotes: ", String1)

# Creating a String
# with triple Quotes
String1 = '''I'm Learning Python and I "Python" is easy to learn'''
print("String with the use of Triple Quotes: ", String1)


# Creating String with triple
# Quotes allows multiple lines
String1 = '''I'm Learning Python 
            "Python" is easy to learn
          '''
print("Creating a multiline String: ", String1)

# Accessing characters in Python String
'''
In Python, individual characters of a String can be accessed by using the method of Indexing. 
Indexing allows negative address references to access characters from the back of the String, 
e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 
While accessing an index out of the range will cause an IndexError. 
Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError.
'''

# Example
string = "Python"
#Positive indexing(starts with 0)
print(string[0]) # prints p
print(string[1]) # prints y
print(string[2]) # prints t
print(string[3]) # prints h
print(string[4]) # prints o
print(string[5]) # prints n

#Negative indexing(starts with -1)
print(string[-6]) # prints p
print(string[-5]) # prints y
print(string[-4]) # prints t
print(string[-3]) # prints h
print(string[-2]) # prints o
print(string[-1]) # prints n

# String Slicing
'''
In Python, the String Slicing method is used to access a range of characters in the String. 
Slicing in a String is done by using a Slicing operator, i.e., a colon (:). 
One thing to keep in mind while using this method is that the string returned after slicing includes the character 
at the start index but not the character at the last index.
'''
#Example:
String = "Python"
print("Sliced string from first to third character: ", string[0:3])

#Reversing a Python String using slice method
'''
By accessing characters from a string, we can also reverse strings in Python. 
We can Reverse a string by using String slicing method.
'''
#Example:
String = "Python"
print("Reverse string from sliced method: ", string[::-1])

#Deleting/Updating from a String
'''
In Python, the Updation or deletion of characters from a String is not allowed. 
This will cause an error because item assignment or item deletion from a String is not supported. 
Although deletion of the entire String is possible with the use of a built-in del keyword. 
This is because Strings are immutable, hence elements of a String cannot be changed once assigned. 
Only new strings can be reassigned to the same name. 
'''

# Updating a character
'''
A character of a string can be updated in Python by first converting the string into a Python List and then updating the element in the list
As lists are mutable in nature, we can update the character and then convert the list back into the String.
Another method is using the string slicing method. Slice the string before the character you want to update, 
then add the new character and finally add the other part of the string again by string slicing.
'''

# Example
string = 'Py'
List = list(string)
List[1] = 'ython'
string = ''.join(List)
print("Updated string:", string)

#using slice method
String1 = "Hello, world"
String3 = String1[0:7] + 'beautiful' + String1[6:]
print(String3)

#Updating Entire String
'''
As Python strings are immutable in nature, we cannot update the existing string. 
We can only assign a completely new value to the variable with the same name.
'''

#Example:
language = "Python"
print(language)
# assigning the new value for the same variable
language = "Java"
print(language)

#Deleting a character
'''
Python strings are immutable, that means we cannot delete a character from it. 
When we try to delete thecharacter using the del keyword, it will generate an error.
But using slicing we can remove the character from the original string and store the result in a new string.
'''

language = "Python"
#del(language[1])  will throw an error 'str' object doesn't support item deletion so commenting
#print(language)

#Deleting Entire String
'''
Deletion of the entire string is possible with the use of del keyword.
Further, if we try to print the string, this will produce an error because the String is deleted and is unavailable to be printed. 
'''
# del(language)
# print(language) will throw an error NameError: name 'language' is not defined so commenting

#Escape Sequencing in Python
'''
While printing Strings with single and double quotes in it causes SyntaxError because String already contains Single and Double Quotes and hence cannot be printed with the use of either of these. 
Hence, to print such a String either Triple Quotes are used or Escape sequences are used to print Strings. 
Escape sequences start with a backslash and can be interpreted differently. 
If single quotes are used to represent a string, then all the single quotes present in the string must be escaped and the same is done for Double Quotes. 
'''

String1 = 'I\'m Learning "Python"'
print("Escaping Single Quote: ",String1)

#Ignoring the escape sequence
'''
To ignore the escape sequences in a String, r or R is used, 
this implies that the string is a raw string and escape sequences inside it are to be ignored.
'''
string = r'I\'m Learning "Python"'
print("Printing string with escape character: ", string)

# Formatting of strings
'''
Strings in Python can be formatted with the use of format() method 
which is a very versatile and powerful tool for formatting Strings. 
Format method in String contains curly braces {} as placeholders which 
can hold arguments according to position or keyword to specify the order.
'''
#Example: using format method
string = "{} is very easy".format("Python")
print("Print String in using format method: ", string)
string = "Python is easy"
print(f'{string}')

# Length of the string
'''
The len() function returns the length of the string. 
'''

language = "Python"
print(len(language)) # outputs 6 as python has 6 characters

# String Slicing in Python
'''
Python slicing can be done in two ways:
Using a slice() method
Using the array slicing  [:: ] method
'''

# Method 1: Using the slice() method
'''
Syntax: slice(start, stop, step)
'''
# Example:
name = "Python"
# creating a slice constructor
Slice = slice(0,2,1)
print("String slicing using slice function", name[Slice])

# Method 2: Using the List/array slicing  [ :: ]  method
'''
Syntax: var_name[start:stop:step]
'''
name = "Python"
print("String slicing using List/array slicing", name[0:2:1])



