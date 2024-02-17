#1. Program to reverse a number
Number = int(input("Enter the Number: ")) # Taking input from the user
def reverse_number(number): # defining a function which takes one argument
    reversed_number = 0
    while number > 0:
        reversed_number = reversed_number * 10 + number % 10
        number = number//10
    print(reversed_number)

# Calling a function
reverse_number(Number)

#2. Program to check whether given integer is armstrong or not
'''
It is a number that is equal to the sum of its own digits raised to the power of the number of digits.
For eg: 153, is an Armstrong number because it has 3 digits, and 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
'''

# using while loop
Number = int(input("Enter the Number: ")) # Taking input from the user
Sum = 0
temp_num = Number
len_num = len(str(Number))
while Number > 0:
    single_no = Number % 10
    Sum = Sum + single_no ** len_num
    Number = Number // 10
if temp_num == Sum:
    print("Armstrong")
else:
    print("Not a Armstrong Number")

# using list comprehension
no = 153
digits = [int(i) for i in str(no)]
sum = sum([i ** len_num for i in digits])
if no == sum:
    print("Armstrong")
else:
    print("Not a Armstrong Number")


#3. Program to check the given number is prime or not
'''
In Mathematical terms, A prime number is a natural number greater than 1 that can be divided by only 1 and the number itself.
For example 2, 3, 5, 7, 13… are Prime numbers.
'''
Number = int(input("Enter the Number: "))
temp = 0
for i in range(2,Number):
    if Number % i == 0:
        temp = 1
        break
if temp == 1:
    print("Not Prime")
else:
    print("Prime")

# Fibonacci Series in Python
Number = 10
Initial_List = [0,1]
for i in range(0,Number):
    Initial_List += [Initial_List[i] + Initial_List[i+1]]
print(Initial_List) # prints the fibonacci series in list
first = 0
second = 1
for i in range(0, Number):
    if i <= 1:
        result = i
    else:
        result = first + second
        first = second
        second = result
    print(result)


#sum of digits
Number = 10
sum = 0
for i in range(11):
    sum = sum + i
print(sum)

# Program to swap two number
a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b); 