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

def combinations(n, k): # nCk
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))

# print(combinations(52, 5))




'''
Combinations Intuition
An expensive Counting Approach
Ex:

Out of a set of 11 basketball players, only
5 can be on the court at a time. What are all
the combinations possible for that basketball team.
'''

num_combs = combinations(11, 5)

# print(num_combs)

def basketball_combs():
    eleven_nums = list(range(1, 11+1))

    # counting in base 5
    possible_five = []

    for i in eleven_nums:
        for j in eleven_nums:
            for k in eleven_nums:
                for l in eleven_nums:
                    for m in eleven_nums:
                        possible_five.append([i,j,k,l,m])

    # for five in possible_five:
    #     print(five)

    perms = []

    for five in possible_five:
        if len(list(set(five))) == 5:
            perms.append(five)

    # for five in perms:
    #     print(five)
     
    combs = []

    for five in perms:
        sorted_five = sorted(five)

        if sorted_five not in combs:
            combs.append(sorted_five)

    return combs

# five_combs = basketball_combs()

# for five in five_combs:
#     print(five)

# print()
# print(len(five_combs))
# print(combinations(11, 5))


'''
A slightly less expensive Sampling approach

We can sample 5 players from our list of 11
until we reach 11C5 combinations
'''

from random import choice

def basketball_combs_samp(team_size=11, num_players=5):
    combs = []

    player_range = range(1, team_size+1)

    while len(combs) < combinations(team_size, num_players):
        player_comb = []

        while len(player_comb) < num_players:
            player_num = choice(player_range)

            if player_num not in player_comb:
                player_comb.append(player_num)

        player_comb = sorted(player_comb)

        if player_comb not in combs:
            print(player_comb)
            combs.append(player_comb)
    return combs

# team_size = 21
# num_players = 5

# print(len(basketball_combs_samp(team_size, num_players)))
# print(combinations(team_size, num_players))


'''
Combinations based on Itertools algorithm
'''

def combs_alg_from_itertools(lst, k):
    # get a frozen version of input
    lst_frozen = tuple(lst)
    n = len(lst_frozen)

    # fault control
    if k > n:
        return 

    indices = list(range(k))

    yield tuple(lst_frozen[i] for i in indices)

    while True:
        for i in reversed(range(k)):
            if indices[i] != i + n-k:
                break
        else:
            return
        
        indices[i] += 1
        for j in range(i+1, k):
            indices[j] = indices[j-1] + 1

        yield tuple(lst_frozen[i] for i in indices)

player_range = range(1, 21+1)

# c = list(combs_alg_from_itertools(player_range, 5))

# for comb in c:
#     print(comb)




'''
https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introStats/04_Basic_Probability/04_permutations.md

Ch 3
'''

elems = list('abcdefghijklmnopqrstuvwxyz0123456789')

ss = []

for e1 in elems:
    for e2 in elems:
        for e3 in elems:
            ss.append([e1,e2,e3])

perms = []

for outcome in ss:
    if len(list(set(outcome))) == 3:
        perms.append(outcome)

# for perm in perms:
#     print(perm)

print(len(perms))