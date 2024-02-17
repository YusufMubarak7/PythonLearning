# Different ways of reversing the string
Name = "Python"
# Using extended slice
print(Name[::-1]) #This will print the reversed string.

#Using For Loop
rev = ''
for i in Name:
    rev = i + rev
print(rev) #This will print the reversed string.

#Using List Comprehension
def reverse(string):
    string = [string[i] for i in range(len(string)-1, -1, -1)]
    print("".join(string))


reverse(Name)

# using reversed method
rev_str = "".join(reversed(Name))
print(rev_str)

#Using recursion
def reverse_recur(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recur(s[1:]) + s[0]

reverse_recur(Name)