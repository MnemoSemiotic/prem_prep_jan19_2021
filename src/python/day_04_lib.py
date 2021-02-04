
""" ########################################
# types
    # types we've covered
    # int, float, bool, str, None
    # list
    # tuple, dict, set

# functions
    # capture a process and let us reuse it

# conditions
    # if, elif, else
    # run code of some "condition" is True
    # else not run any special or run some other code

# loops
    # reapeat some process


def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num

    return prod


print( factorial(4) ) # 24
print( factorial(5) ) # 120
print( factorial(6) ) # 720
######################################## """
""" ########################################

x = 9
why does `x` equal 9

```
def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num

    return prod
```


######################################## """
""" ########################################

'''
* What are the 4 scalar types we briefly discussed?
    # int, float, bool, str
* What does print(1/100**100000) give us and why?
    # underflow error / rounding error
* What does 3 == 3 evaluate to?
    # True
* What does 2 != 2 evaluate to?
    # False
'''


######################################## """
""" ########################################

# What response will this code produce when:
def breakout2(x):
    if x % 2 == 0 and x % 5 == 0:
        return 'Gimme 10!'
    elif x % 5 == 0:
        return 'High Five!'
    elif x % 2 == 0:
        return 'Evens!'
    else:
        return "I got nothing"


x = 9
print( breakout2(x) )
x = 80
print( breakout2(x) )
x = 25
print( breakout2(x) )
x = 66
print( breakout2(x) )

######################################## """
""" ########################################

# print( "this string is my argument to print" )
input("input a number")
input("input another number")

######################################## """
""" ########################################

def add_nums(a, b):
    return a + b

ten = add_nums(3, 4) + 3
print(ten)

######################################## """
""" ########################################

def factorial(n):
    prod = 1
    for poodles in range(1, n+1):
        prod *= poodles

    return prod


print( factorial(n) )

######################################## """
""" ########################################

def add_nums(a=10, b=10):
    return a + b


# print( add_nums() )
print( add_nums(4) )
print( add_nums(4, 3) )

######################################## """
""" ########################################

name = "Sally"
age  = 39
print(f"{name} is {age} years old")
# print(name, " is ", age, " years old")


######################################## """
""" ########################################

def welcome_message(name):
    return f'Hello {name}!'


name_1 = input('Please enter your name: ')
# name_1 = "Clark"
print(welcome_message(name_1))

######################################## """
""" ########################################

y = 20
def add_nums(a, b):
    y = 20
    return a + b + y


y = "horse"
print(add_nums(1, 2))

######################################## """
""" ########################################

lst = [3, 6, 1, 9, 5.4]
# print( lst[0] )
# print( lst[-5] )
# print( lst[1] )
# print( lst[-4] )
# print( lst[2] )
# print( lst[-3] )

# print( lst[5] )

n = 8
my_range = list( range(4, n+1) )
print(my_range)
my_range = list( range(5) )
print(my_range)
my_range = list( range(n+1) )
print(my_range)

######################################## """
""" ########################################

my_range = range(5)
print(my_range)

######################################## """
""" ########################################

# not and or
lst = [6, 2, 4, 3, 8, 0, 1, 2, 2]
if "hello" not in lst:
    print("hello not in lst")

######################################## """
""" ########################################

lst = [6, 2, 4, 3, 8, 0, 1, 2, 2]
print( lst[2 : 7+1: 2] )

print( lst[2::] )
print( lst[:4+1:] )
print( lst[::-1] ) # reverses a list
print( lst[::] ) # reverses a list

######################################## """
""" ########################################

def add_nums(a, b):
    return a + b


######################################## """
""" ########################################

# star args
def whatcha_got( *args ):
    answers = []
    for num in args:
        if num % 5 == 0:
            answers.append('High Five!')
        elif num % 2 == 0 and num % 5 == 0:
            answers.append('Gimme 10!')
        elif num % 2 == 0:
            answers.append('Evens!')
        else:
            answers.append("I got nothing")

    return answers


x = [9, 80, 25, 66]
print( whatcha_got(*x) )

######################################## """
# """ ########################################


######################################## """
# """ ########################################


######################################## """
# """ ########################################


######################################## """
# """ ########################################


######################################## """
# """ ########################################


######################################## """
# """ ########################################


######################################## """
# """ ########################################


######################################## """
