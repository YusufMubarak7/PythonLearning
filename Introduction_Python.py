'''
Programming: It is a set of instruction in the form of code which will tell the computer to perform specific tasks.
All the code will be processed by processor which understands only binary language.To convert Programming Language into binary language we make use of translator

Types of Translator
Compiler -> Converts Entire code to binary at once
Interpretor -> line by line code is converted to binary

Python: Python is an object-oriented programming language created by Guido Rossum in 1989.

Features of Python
Platform Independent
Dynamically typed language(size and type need not to be specified)
Number of lines of code is less and more efficient
Open source(www.python.org)
Interpretted language

install Python on Windows:

Step 1: To download and install Python, visit the official website of Python https://www.python.org/downloads/ and choose your version.
Step2:  Once the download is completed, run the .exe file to install Python. Now click on Install Now.(Make sure to check Add Python to PATH)
Step3: When it finishes, you can see a screen that says the Setup was successful. Now click on “Close”.


'''

''' First Python Program '''
print("Hello world") #This line will print Hello world

''' Comments in Python'''
'''Comments starts with a #, and Python will ignore them:'''

''' Introduction to Variables '''
''' 
Variables are containers for storing data values.
Creating Variables
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
Variables do not need to be declared with any particular type, and can even change type after they have been set.
Variables are case sensitive that means Name and name are two different variables
Multiple variable creation 
Ex: a,b,c,d = 1,2,3,4 
Note: Number of variables and values should be same in case of multiple variable creation
Ex: a,b,c = 1,2,3,4 (This will throw error as number of variables and values are not equal)
One Value to Multiple Variables: And you can assign the same value to multiple variables in one line:
Ex: a = b = c = 10
'''

#Examples
Number = 10
Language = "Python"

''' Get the type of variable'''
'''
You can get the data type of a variable with the type() function.
'''
print(type(Number)) #This will print class 'int'
print(type(Language)) #This will print class 'str'

'''Rules of Variables'''
'''
1.A variable name must start with a letter or the underscore character
2.A variable name cannot start with a number
3.A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
4.A variable name cannot be any of the Python keywords.
'''

# Legal Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Python Output Variables
# The Python print() function is often used to output variables.
# In the print() function, you output multiple variables, separated by a comma:
# Syntax Print(var1,var2,var3, sep =str, end =ste)

# Example:
print(1,2,3, sep='\n', end="\n")

# Python Input Variables
# The Python input() function is often used to take input from users.
# The return type of input() function will always be string
# Syntax input("Message") where writing message is not mandatory

# Example
Name = input('Enter your name: ')
print(Name)

# we can change the return type of input function using type caste
# Example
Number = int(input('Enter any number: '))
print(Number)
print(type(Number)) # type will be int as we have type casted the input function to int
