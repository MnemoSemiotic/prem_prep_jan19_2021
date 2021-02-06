

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

