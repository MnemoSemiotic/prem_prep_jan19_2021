""" un/comment to de/activate ################

# print( set([6, 3, 6, 4]) )

set1 = set('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.'.lower().replace('.', '').split(' '))

set2 = set('Complex is better than complicated. Flat is better than nested. Sparse is better than dense.'.lower().replace('.', '').split(' '))
print(set1)
print(set2)
print()
print(set1.intersection(set2))
print()
print(set1.union(set2))
print()
print(set1 - set2) # elements exclusive to set1
print()
print(set2 - set1) # elements exclusive to set2

########################################## """
""" un/comment to de/activate ################

print( dir(list) )
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
print( dir(tuple) )
'count', 'index'

########################################## """
""" un/comment to de/activate ################

'''
Write a function that prompts the user to input numbers separated by dashes ( - ).

Your script will take those numbers, and print a dictionary where the keys are the inputted numbers, and the values are the squares of those numbers.

Example: If you inputted the numbers "1 - 5 - 8 - 10", your script should print {8: 64, 1: 1, 10: 100, 5: 25} (remember that dictionaries are unordered, which is why the script might print out the key-value pairs in a different order than the user inputted the numbers).
'''
def square_nums_d(inp=False):
    if not inp:
        inp = input("input numbers seperated by '-': ")
    lst = inp.split("-")

    d = {}
    for num_ch in lst:
        d[int(num_ch)] = int(num_ch)**2
        # print(int(num_ch)**2)

    return d


print( square_nums_d() )
# print( square_nums_d("1 - 5 - 8 - 10") )
# print( square_nums_d("14 - 577 - 8 - 10") )
# {8: 64, 1: 1, 10: 100, 5: 25}

########################################## """
""" un/comment to de/activate ################

def num_chars(txt):
    '''
    function that takes in a string and parses through
    identifying how many characters are in each word,
    assuming a whitespace is what separates your words
    parameters:
        s: str - a string

    returns:
        A dictionary, where the keys are the words and the
        values are the number of characters in each word
    '''
    d = {}
    for word in txt.lower().split():
        d[word] = len(set(word))

    return d


my_text = '''
Whose woods these are I think I know
His house is in the village though
He will not see me stopping here
To watch his woods fill up with snow'''


print(num_chars(my_text))
########################################## """
""" un/comment to de/activate ################

names = ["Jane", "Jessie", "Joanne"]
ages  = [54, 29, 33]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

########################################## """
""" un/comment to de/activate ################

# APR Arguments, Process, Return
input("type a number:")

########################################## """
""" un/comment to de/activate ################
'''
Write a function that prompts the user to input numbers separated by commas.

Your script will then take these inputted numbers and store them as a list of tuples, two at a time.

Use the zip() function to do this. If the user inputs an odd number of numbers, then only make a list of the largest number of pairs of two that are possible.

Example:
If you inputted the numbers '1, 2, 3, 4, 5, 6', your function should return [(1, 2), (3, 4), (5, 6)]. If you inputted the numbers 1, 2, 3, 4, 5, your function should return [(1, 2), (3, 4)].
'''

def tupleator(inp=False):
    if not inp:
        inp = input("comma seperated numbers")

    itr_lst = inp.split(",")
    lst = []
    for a, b in zip(itr_lst[::2], itr_lst[1::2]):
        lst.append((int(a), int(b)))

    return lst


print( tupleator("3, 4, 6, 2") )
# [(3, 4), (6, 2)]
print( tupleator("1, 2, 3, 4, 5, 6") )
# [(1, 2), (3, 4), (5, 6)]
print( tupleator("1, 2, 3, 4, 5") )
# [(1, 2), (3, 4)]

########################################## """
""" un/comment to de/activate ################

old_lst = [1, 2, 3, 4, 5, 6]
new_lst = []
for i in old_lst:
    new_lst.append(i**2)

new_lst = [ i ** 2 for i in old_lst ]

########################################## """
""" un/comment to de/activate ################

new_lst = []
for i in old_lst:
    if i > 10:
        new_lst.append(i**2)

new_lst = [i ** 2 for i in old_lst if i > 10]


new_lst = []
for i in old_lst:
    if i > 10:
        new_lst.append(i**2)
    else:
        new_lst.append(i//2)


i**2 if i > 10 else i//2 if i < 5 else i * 3

new_lst = [i ** 2 if i > 10 else i//2 for i in old_lst]


new_dict = {}
for i in old_lst:
    new_dict[i] = i**2

new_dict = {i:i**2 for i in old_lst}
########################################## """
# """ un/comment to de/activate ################



########################################## """
