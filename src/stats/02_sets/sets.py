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


'''
Set Union
'''
list1 = ['astronomy', 'nanoscience', 'datascience', 'biochemistry', 'sociology', 'chemistry', 'botony']
list2 = ['psychology', 'chemistry', 'botony', 'bioengineering', 'robotics', 'computer science',]
list3 = ['computer science', 'nanoscience', 'datascience', 'psychology', 'botony']


def union(set1, set2):
    set_union = set1.copy()

    for item in set2:
        if item not in set_union:
            set_union.append(item)
    return set_union

# print(union(list1, list2))


'''
Star Args (*args)
'''

def star_args(*args):
    print(type(args))
    for item in args:
        print(item)
    return None

# star_args('hi', 3.1415, 'dog', 'cat', 89702089, True, None, [6,5,4,9,8,7])


def union_mult_sets(*mult_sets):
    set_union = []

    for lst in mult_sets:
        for item in lst:
            if item not in set_union:
                set_union.append(item)

    return set_union

# print(list1, list2, list3)
# print(union_mult_sets(list1, list2, list3))


'''
Intersection
'''

def intersection(set1, set2):
    set_intersect = []

    for item in set1:
        if item in set2:
            set_intersect.append(item)
    return set_intersect

# print(intersection(list1, list2))


def intersection_mult(*mult_sets):
    set_intersect = []

    if len(mult_sets) > 1 and len(mult_sets[0]) > 0:
        for item in mult_sets[0]:
            is_member = True

            for set_ in mult_sets[1:]:
                if item not in set_:
                    is_member = False
                    break
            if is_member:
                set_intersect.append(item)
    return set_intersect
        
# print(intersection_mult(list1, list2, list3))


'''
Set Difference
'''

def difference(set1, set2):
    set_difference = []

    for item in set1:
        if item not in set2:
            set_difference.append(item)
    return set_difference

# print(difference(list1, list2))
# print(difference(list2, list1))



'''
Complement
'''

list1 = ['astronomy', 'nanoscience', 'datascience', 'biochemistry', 'sociology', 'chemistry', 'botony']
list2 = ['psychology', 'chemistry', 'botony', 'bioengineering', 'robotics', 'computer science',]
list3 = ['computer science', 'nanoscience', 'datascience', 'psychology', 'botony']

extra_stuff = ['radiology', 'astrophysics']

sample_space = union_mult_sets(list1, list2, list3, extra_stuff)

# print(sample_space)

['astronomy', 'nanoscience', 'datascience', 'biochemistry', 'sociology', 'chemistry', 'botony', 'psychology', 'bioengineering', 'robotics', 'computer science', 'radiology', 'astrophysics']

def complement(sample_space, set1):
    return difference(sample_space, set1)

# print(complement(sample_space, list1))



'''
Breakout

Which of the following would not be considered a random experiment? Why?

A. The selection of a numbered ball from a bucket of numbered balls (1-50)
B. The amount of time needed to wait for a taxi cab
C. Randomly selecting a colored marble from an urn full of numbered balls
'''



'''
Write out the sample space for the random experiment which is defined as sequentially completing the following steps:

1. First, rolling a four-sided die
2. Then, flipping a coin
3. And finally, flipping the coin a second time

'''

outcomes = []

for die_roll in range(1, 4+1):
    for flip1 in ['H', 'T']:
        for flip2 in ['H', 'T']:
            outcomes.append([die_roll, flip1, flip2])

# for outcome in outcomes:
#     print(outcome)





'''


List the sample points in the following events:
A = The event in which the die roll results in exactly one pip showing
B = The event in which at least one of the coin flips results in heads

List the sample points which are in the Union of events A and B from above
'''
