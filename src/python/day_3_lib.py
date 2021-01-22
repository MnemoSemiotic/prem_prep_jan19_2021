""" ########################################

# this is invalid code
x += 1
print(x) #NameError: name 'x' is not defined

########################################### """
""" ########################################

# this is valid code
x = 3
x += 1
print(x)

########################################### """
""" ########################################

# True False
a = 3
b = 5
print(3 == 5)
a, b, c = 11, 22, 33
a = 11
b = 22
c = 33

########################################### """
""" ########################################

# animals_lst = ["cat", "dog"]

########################################### """
""" ########################################
# int, flot, bool, str

print(5 > 5)
print(5 >= 5)
print(5 < 5)
print(5 <= 5)
print(5 == 5)
print(5 != 5)

########################################### """
""" ########################################

print(not True)  # False
print(not False) # True

print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False


########################################### """
""" ########################################

a, b, c, d = 3, 5, 3, 7
print( (a < b) and (c == a) ) # Ture ;)
print((not (not (True or False) and (True and True))) and True or True) # True

########################################### """
""" ########################################

# OR
print(True or True) # True  <----------|
print(True or False) # True            |
print(False or True) # True            |
print(False or False) # False          |
#                                      |
# XOR                                  |
print(True ^ True) # False  <----------|
print(True ^ False) # True
print(False ^ True) # True
print(False ^ False) # False

########################################### """
""" ########################################
not 7 > 2 #False

3 >= 2 or 5 < 1 # True

not 8 # False

bool('') and 5 != 3 # False

bool('') and 5 != 5 # False

########################################### """
""" ########################################

a = 10
b = 10
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

c = 10
if a == c:
    print("a and c are equal")
if a == b:
    print("a and b are equal")

########################################### """
""" ########################################

a, b, c, = 3, 3, 3

if (a == b) and (a == c):
    print("b and c are equal")


if a == b:
    print("a is equal to b")
    if a == c:
        print("b and c are equal")


if a == b == c:
    print("they're all equal")


if (a == b) and ("hello" == "tomato"):
    pass


def factorial(n):
    '''
    factorial returns the product of every number between 1 and n including n

    n: int
        the number to take the factorial of

    returns:
        prod: int
            the factorial of n
    '''
########################################### """
""" ########################################
'''
* Write a code snippet that checks two numbers, `x` and `y`:
    * if the sum of two numbers is greater than both numbers
        * print `"Both numbers are positive"`
    * if the sum is equal to either number
        * print `"At least one number is zero"`
    * else:
        * print `"At least one number is negative"`
'''

def compare_number(x, y):
    if ((x + y) > x) and ((x + y) > y):
        print("Both numbers are positive")
    elif ((x + y) == x) or ((x + y) == y):
        print("At least one number is zero")
    else:
        print("At least one number is negative")


# positive
a = 6
b = 6
compare_number(a, b) # Both numbers are positive

# 1 negative
a = 6
b = -3
compare_number(a, b) # At least one number is negative

# 2 negative
a = -6
b = -3
compare_number(a, b) # At least one number is negative

# 1 zero
a = 6
b = 0
compare_number(a, b) # At least one number is zero

# 2 zeros
a = 0
b = 0
compare_number(a, b) # At least one number is zero

########################################### """
""" ########################################

while True:
    x = input('Please enter a whole number:')
    y = input('Please input a second number:')
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        break

    print("x and y need to be numbers try again")

if x + y > x or y:
    print('Both numbers are positive')

elif x + y == x or y:
    print('At least one number is zero')

else:
    print('At least one number is negative')





########################################### """
# """ ########################################



########################################### """
# """ ########################################



########################################### """
# """ ########################################



########################################### """
