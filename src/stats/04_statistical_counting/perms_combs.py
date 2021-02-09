from math import factorial

def factorial(n):
    prod = 1

    for num in range(2, n+1):
        prod *= num

    return prod

# def factorial(x): 
#     if x == 1: return x 
#     else: return x * factorial(x-1)

# print(factorial(5))
# print(factorial(0))


'''
There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?

Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?
'''
# print(factorial(10))
# card_S = factorial(10)
# card_A = 1
# print(card_A / card_S)


'''
Permutations
'''

def permutation(n, k):
    return int(factorial(n) / factorial(n-k))


def permutation(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm



'''
Five pets and 5 beds. What are all the ways that you can
arrange those 5 pets in 5 beds?
'''

base_5 = ['bat', 'cat', 'frog', 'eel', 'hamster']

animals_counting = []

for an1 in base_5:
    for an2 in base_5:
        for an3 in base_5:
            for an4 in base_5:
                for an5 in base_5:
                    animals_counting.append([an1, an2, an3, an4, an5])

# for an_number in animals_counting:
#     print(an_number)

animal_perms = []

for an_number in animals_counting:
    perm = True

    for an in an_number:
        if an_number.count(an) > 1:
            perm = False
            break

    if perm:
        animal_perms.append(an_number)

# for an_number in animal_perms:
#     print(an_number)


'''
Permutation using non-recursive Heaps algorithm
'''



def swap(lst, idx_1, idx_2):
    lst_ = lst.copy()
    temp = lst_[idx_2]
    lst_[idx_2] = lst_[idx_1]
    lst_[idx_1] = temp
    return lst_

# print(swap(base_5, 0, 3))

def heaps_non_recursive(lst, k):
    # avoid modifying parameter
    lst_copy = lst.copy()

    # holds stack state
    c = [0] * len(lst)

    # collect permutations, collect initial perm
    perms = [lst_copy[:k]]

    i = 0 # acts like a stack pointer
    while i < len(lst_copy):
        if c[i] < i:
            if i % 2 == 0:
                lst_copy = swap(lst_copy, 0, i)
            else:
                lst_copy = swap(lst_copy, c[i], i)
            
            if lst_copy[:k] not in perms:
                perms.append(lst_copy[:k])

            # incr the counter
            c[i] += 1

            # reset i
            i = 0
        else:
            # reset state of count state at i
            c[i] = 0
            i += 1

    return perms

# base_5 = ['bat', 'cat', 'frog', 'eel', 'hamster']

# perms = heaps_non_recursive(base_5, 4)

# for perm in perms:
#     print(perm)

# print()
# print(len(perms))
# print(permutation(5, 4))


'''
Combinations
'''

def combinations(n, k): # nCk
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

# def combinations(n, k): # nCk
#     perm = 1
#     for i in range(n, n-k, -1):
#         perm *= i
#     return int(perm / factorial(k))

print(combinations(52, 5))