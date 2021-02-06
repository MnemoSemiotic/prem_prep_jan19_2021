

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



