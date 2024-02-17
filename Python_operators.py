# Operators in Python
'''

1.Arithmetic Operators
2.Comparison Operators
3.Logical Operators
4.Assignment Operators
5.Identity Operators
6.Membership Operators
7.Bitwise Operators

'''

# Arithmetic Operators( Works for all single value datatypes or Numbers)
'''
Python Arithmetic Operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.
'''
#1.Addition operator(+) = It is used to add two or more operands
#Example
number = 10
Number = 10.0
sum = number + Number
print(sum)

#2.Subtraction operator(-) = It is used to subract two or more operands
#Example
number = 10
Number = 11
sub = number - Number
print(sub)

#3.Multiplication operator(*) = It is used to two or more operands
#Example
number = 10
Number = 11
mul = number * Number
print(mul)

#3.Divison operator(/) = It is used to divide the first operand by the second
#Example
number = 10
Number = 3
div = number/Number
print(div) # Output will be 3.3333333333333335 the output will be float

#4.Floor Divison(//) = It is used to divide the first operand by the second
#Example
number = 10
Number = 3
div = number//Number
print(div) # Output will be 3 as floor divison will give output as int

#5.Modulus Operator(%) = It returns the remainder when the first operand is divided by the second
#Example
number = 129
Number = 10
rem = number % Number
print(rem) # Output will be 9

#6.Exponential operator(**) = In Python, ** is the exponentiation operator. It is used to raise the first operand to the power of the second.
Number = 10
pow = Number ** 2
print(pow)

#Comparison Operators
'''
Relational operators are used for comparing the values. It either returns True or False according to the condition. 
These operators are also known as Comparison Operators.
'''

#1.Greater than(>): True if the left operand is greater than the right
#Example
number = 1
Number = 0.95
print(number > Number) # output is true

#2. Less than(<): True if the left operand is less than the right
#Example
number = 1
Number = 0.95
print(Number < number) # output is true

#3. Equal to(==): True if both operands are equal
#Example
number = 1
Number = 0.95
print(Number == number) # output is false

#4. Not equal to(!=): True if operands are not equal
#Example
number = 1
Number = 0.95
print(Number != number) # output is true

#5.Greater than or equal to(>=): True if left operand is greater than or equal to the right
number = 1
Number = 1
print(Number >= number) # output is true

#6. Less than or equal to(<=): True if left operand is less than or equal to the right
number = 1
Number = 12
print(Number <= number) # output is false

# Logical Operators
'''
In Python, Logical operators are used on conditional statements (either True or False). 
They perform Logical AND, Logical OR, and Logical NOT operations.
'''

#1. and Operator: Returns True if both the operands are true
number = 1
Number = 12
print(Number > 10 and number < 10) # output is true

#. or Operator: Returns True if either of the operands is true
number = 1
Number = 12
print(Number < 10 or number < 10) # output is true

#. not Operator: Returns True if the operand is false
number = 1
print(not number > 10)

# Membership Operators
'''
Python offers two membership operators to check or validate the membership of a value. 
It tests for membership in a sequence, such as strings, lists, or tuples. 
'''

#1. in operator: The ‘in’ operator is used to check if a character/ substring/ element exists in a sequence or not.
# Evaluate to True if it finds the specified element in a sequence otherwise False.
#Example:
Name = "Python"
Collection = ["Python", "Java", "C"]
print('t' in Name) # true since t is member
print('C++' in Collection) # false as c++ is not a member

#2. ‘not in’ operator- Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.
#Example:
Name = "Python"
Collection = ["Python", "Java", "C"]
print('t' not in Name) # false since t is memberwq
print('C++' not in Collection) # true as c++ is not a member

# Identity Operator:
'''
Identity operators are used to compare the objects if both the objects are actually of the same data type and share the same memory location.
There are different identity operators such as 
'''

#1. ‘is’ operator – Evaluates to True if the variables on either side of the operator point to the same object and false otherwise.
#Example:
x = 5
y = 5
print(x is y) # true both the variables x and y have value 5 assigned to it and both share the same memory location, which is why return True.

# Assignment Operators in Python(It's easy so not covering)
'''
 Refer https://www.geeksforgeeks.org/assignment-operators-in-python/
 for Assignment operators like ( =, =+, =-, *=, /=, %=, //=, **=, &=,|=, ^=, >>=, <<=)
'''

# Bitwise Operators(Not so important so not covering)
'''
Refer https://www.geeksforgeeks.org/python-bitwise-operators/ for Bitwise Operators
'''



