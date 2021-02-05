# """ un/comment to de/activate ################
'''
Write a function called percentile_50 that takes a list of arbitrary numbers The function will return a dictionary

* where the keys are strings that describe the upper and lower 50th percentile (the median) as a range (see below)

* And the values are lists containing numbers from the input list that fall within the lower(inclusive) or upper(also inclusive) percentile described by the key
'''

def median(lst):
    length = len(lst)
    lst = sorted(lst)
    if length % 2 == 1: # odd lenght
        return lst[ int(length / 2) ]
    else: # even length
        lower = lst[ int(length / 2) - 1 ]
        upper = lst[ int(length / 2)]
        return (lower + upper) / 2


def percentile_50(lst):
    med = median(lst)
    d = {"<=0.50": [], ">=0.50": []}
    for num in lst:
        if num <= med:
            d["<=0.50"].append(num)
        if num >= med:
            d[">=0.50"].append(num)

    return d


my_lst = [1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10]
# print( percentile_50(my_lst) )
# {'<=0.50': [1, 5, 8, 5, 0.1, 9], '>=0.50': [234, 64, 44, 746, 9, 10]}

my_lst = [1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10, 1000]
# print( percentile_50(my_lst) )
# {'<=0.50': [1, 5, 8, 5, 0.1, 9], '>=0.50': [234, 64, 44, 746, 10, 1000]}


'''
Modifying what we have built already, let’s try this again, but instead of the 50th percentile, let’s cut our data into quartiles and do the same thing!

Let’s make a function that takes in a list of random numbers (Could be floats or ints) and returns a dictionary which identifies where the numbers appear in terms of quartiles. Assume each quartile mark includes the lower end of the range and goes up to but does not include the upper end of the range.

Step 1: We need to identify the quartiles Using our example list, how would you - in plain words - identify the quartiles? [1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10] Alright, now recall our median code and our code from breakout 1a? How can that be used to identify the quartiles?
'''

def quartiles_d(lst):
    percentile_50_d = percentile_50(lst)
    lower = median(percentile_50_d['<=0.50'])
    med   = median(lst)
    upper = median(percentile_50_d['>=0.50'])

    d = {"<0.25": [], "<0.50": [], "<0.75": [], "<=1.0": []}
    for num in lst:
        if num < lower:     # checked and False
            d["<0.25"].append(num)
        elif num < med:     # checked and True
            d["<0.50"].append(num)
        elif num < upper:   # not checked
            d["<0.75"].append(num)
        else:               # not checked
            d["<=1.0"].append(num)

    return d


my_lst = [1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10]
# print(sorted(my_lst))
# [0.1, 1, 5, 5, 8, 9, 10, 44, 64, 234, 746]
# print( quartiles_d(my_lst) )
########################################## """
# """ un/comment to de/activate ################
'''
Create a function that takes in a number
will "flip a coin" H or T

return the count of times the coin flipped heads and tails as well as a list of what the flips were.
'''

# from random import choice
# from random import randint
# from random import random

# print( choice( range(10) ) )
# takes in choices and returns a choice fairly
# NameError: name 'random' is not defined

# AttributeError: 'builtin_function_or_method' object has no attribute 'choice'

# print(random.randint( 5, 10 ))
# returns an integer within the range given fairly

# print(random.random())
# returns an float between 0 and 1

import random
def coin_flipper(num):
    lst = []
    d = {'heads': 0, 'tails': 0}
    for _ in range(num):
        flip = random.choice(["H", "T"])
        lst.append(flip)
        if flip == "H":
            d["heads"] += 1
        else:
            d["tails"] += 1

    return d, lst


# print( coin_flipper(4) )
# {'heads': 3, 'tails': 1}, ["H", "T", "H", "H"]

########################################## """
# """ un/comment to de/activate ################
'''
Let’s create a function that will return the probability that we will get a Heads exactly k times out of n flips (this is a preview for what you will be going over tomorrow - binomial distribution PMF)

We want to represent the below equation in python, where n is the number of trials, k is the number of successes and p is the probability of a success.
'''
def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num

    return prod


def combinations(n, r):
    return int(factorial(n) / ( factorial(r) * factorial(n - r) ))


def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1 - p)**(n - k))

# flip a coin 10 times
# what's the probability of getting 9 heads
# success case = heads # arbitrary
n = 10
k = 9
p = 0.5 # coin
print( binomial_pmf(n, k, p) )

########################################## """
