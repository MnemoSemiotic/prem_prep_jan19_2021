'''
Random Experiment
'''

from random import choice

def coin_flip():
    return choice(['H', 'T'])

# if the experiment is the outcome of a single coin flip
{'H', 'T'}

# What if our random experiment is in regards 
# to the count of Heads in 20 coin flips?

def twenty_flips():
    flips = []

    for _ in range(20):
        flips.append(coin_flip())

    return flips

# print(twenty_flips().count('H'))








'''
list/set trick
-remove duplicates through sets
'''

lst = [6,5,4,3,2,4,1,6,8,7,9,6,3,5,4,6,9,8,7,6,5,4]

l1 = list(set(lst))

# print(l1)


def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)
    return deduped

# print(lst)
# print(dedupe_in_order(lst))


