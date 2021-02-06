

pets = ['cat', 'dog', 'ferret', 'goldfish']

pet_outcomes = []

for pet1 in pets:
    for pet2 in pets:
        for pet3 in pets:
            for pet4 in pets:
                pet_outcomes.append([pet1, pet2, pet3, pet4])

# for pet_outcome in pet_outcomes:
#     print(pet_outcome)

two_plus_cats = []

for pet_outcome in pet_outcomes:
    if pet_outcome.count('cat') >= 2:
        two_plus_cats.append(pet_outcome)

# for cats in two_plus_cats:
#     print(cats)

# print(len(two_plus_cats) / len(pet_outcomes))


'''
Write a function called series_of_flips.

define one parameter, n, which represents the number of coin flips
return a list of length n containing n random coin flips

'''
from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

def series_of_flips(n):
    return [coin_flip() for _ in range(n)]
    # flips = []
    # for _ in range(n):
    #     flips.append(coin_flip())
    # return flips

# print(series_of_flips(4))



'''
Write a function called four_flip_sample_space that takes 
no arguments. It should return a list of all 
possible outcomes for 4 coin flips.
[
    ['H', 'H', 'H', 'H'],
    ['H', 'H', 'H', 'T'],
    ['H', 'H', 'T', 'H'],
    ['H', 'H', 'T', 'T'],
    ...
    ['T', 'T', 'T', 'T'],
]
'''

def four_flip_sample_space():
    flip = ['H', 'T']
    outcomes = []

    for f1 in flip:
        for f2 in flip:
            for f3 in flip:
                for f4 in flip:
                    outcomes.append([f1, f2, f3, f4])

    return outcomes

outcomes = four_flip_sample_space()

# for outcome in outcomes:
#     print(outcome)

'''
What is the probability that in 4 coin flips, you get exactly 3 heads?
write code that traverses the outcomes and delivers P(3heads) = |3heads| / |outcomes|
A = {HHHT, HHTH, HTHH, THHH} == three_heads
S == outcomes
'''
three_heads = []
for outcome in outcomes:
    if outcomes.count('H') == 3:
        three_heads.append(outcome)

print(three_heads)

print(len(three_heads) / len(outcomes))


