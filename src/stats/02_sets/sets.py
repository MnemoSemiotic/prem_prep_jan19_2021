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

print(sample_space)

['astronomy', 'nanoscience', 'datascience', 'biochemistry', 'sociology', 'chemistry', 'botony', 'psychology', 'bioengineering', 'robotics', 'computer science', 'radiology', 'astrophysics']

def complement(sample_space, set1):
    pass