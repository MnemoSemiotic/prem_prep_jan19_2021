""" un/comment to de/activate ################

# CRUD # Create Read Update Delete
# Create
    # a new list
    # a new element and add id into the list
        # where do you ad it


########################################## """
# """ un/comment to de/activate ################

# appending # add an element to the *END* of the list
# my_lst = []
# print(my_lst)
# my_lst.append(20) # IPO # Input Process Output
# print(my_lst)


# extending
# my_app_lst = [0, 0, 0]
# print(my_app_lst)
# my_app_lst.append([5, 3, 5]) # IPO # Input Process Output
# print(my_app_lst)

# my_ext_lst = [0, 0, 0]
# print(my_ext_lst)
# my_ext_lst.extend([5, 3, 5]) # IPO # Input Process Output
# print(my_ext_lst)

# removing
# lst = [44, 66, 44, 22]
# print(lst)
# ele_to_remove = 44
# for _ in range(lst.count(ele_to_remove)):
#     lst.remove(ele_to_remove)

# print(lst)
# lst.remove(66)
# print(lst)

# pop
# lst = [44, 66, 44, 22]
# print(lst)
# popped_num = lst.pop()
# print(popped_num)
# print(lst)

# lst = [44, 66, 44, 22]
# print(lst)
# popped_num = lst.pop(1)
# print(popped_num)
# print(lst)

# len
# my_str = "hello"
# my_tup = (5, 6)
# my_lst = [44, 66, 44, 22]
# print( len(my_str) )
# print( len(my_tup) )
# print( len(my_lst) )

# sum
# my_lst = [44, 66.4, len("44"), 22]
# print(sum(my_lst))

# sorted
# my_lst = [44, 66, 44, 22]
# print( sorted(my_lst) )
# print( my_lst )

# sort
# my_lst = [44, 66, 44, 22]
# print( my_lst )
# print( my_lst.sort() )
# print( my_lst )

# reversed
# my_lst = [44, 66, 44, 22]
# print( my_lst )
# print( list(reversed(my_lst)) )
# print( my_lst )
# my_lst = [44, 66, 44, 22]
# print( my_lst )
# print( my_lst[::-1] )
# print( my_lst )

# reverse
# my_lst = [44, 66, 44, 22]
# print( my_lst )
# print( my_lst.reverse() )
# print( my_lst )
# print( my_lst.reverse() )
# print( my_lst )

# max and min
# my_lst = [44, 66, 44, 22]
# print(max(my_lst))
# print(min(my_lst))
# print( max(["hello", "hi"]) )
# print( min(["hello", "hi"]) )

# count
# my_lst = [44, 66, 44, 22, "hello", "hello"]
# print( my_lst.count(55) )
# print( my_lst.count(44) )
# print( my_lst.count(66) )
# print( my_lst.count("hello") )

# any all
# truthy and falsy
# if 5:
#     print("hello")
# print( bool(0.00000) )
# my_lst = [44, 66, 44, 22]
# print(any(my_lst)) # True
# my_lst = [0, 66, 44, 22]
# print(any(my_lst)) # True
# my_lst = [0, 0, 0, 0]
# print(any(my_lst)) # False

# my_lst = [44, 66, 44, 22]
# print(all(my_lst)) # True
# my_lst = [0, 66, 44, 22]
# print(all(my_lst)) # False
# my_lst = [0, 0, 0, 0]
# print(all(my_lst)) # False

# enumerate

# my_lst = [44, 66, 44, 22]
# for idx, elem in enumerate(my_lst):
#     print(elem*idx)

# zip, (parallel lists)
# names = ["Jen", "Jane", "Joe"]
# ages  = [44, 28, 19]
# cities = ["Denver", "Seattle", "Austin"]
# for name, age, place in zip(names, ages, cities):
#     print(f"{name} is {age} years old, they're from {place}")

# unpacking
# a, b, c = [4, 2, 7]

########################################## """
""" un/comment to de/activate ################

# loops # repeate some process
# conditions


n = 10
controller = 0
while controller < n:
    controller += 1
    print(controller)

########################################## """
""" un/comment to de/activate ################

def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def next_prime(n):
    i = n + 1
    while not is_prime(i):
        i += 1

    return i


def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n


# primes_lst = [17 ,19 ,23 ,29 ,31 ,37 ,41 ,43 ,47]
print( next_prime(31) ) # 37
print( next_prime(32) ) # 37
print( next_prime(37) ) # 41

########################################## """
""" un/comment to de/activate ################

for _ in range(100_000):
# while condition:

########################################## """
# """ un/comment to de/activate ################

# immutable
# +, *
# print("hello " + "world")

# casting to and from
# my_string = str([5, 3, 7])
# print( len(my_string) )
# print( int("hello") )
# print( float("4.3") )
# print( float("4.3") )

# same as lists
    # indexing, slicing
    # enumerate()
    # zip()
    # len()
    # .count()
    # checks for membership
    # "hey" in "hello"

# case transforms
    # .lower(), .upper(), .swapcase(), .capitalize()
# my_string = "Hey There"
# print(my_string.lower())
# print(my_string.upper())
# print(my_string.capitalize())
# print(my_string.swapcase())
# print(my_string)

# f strings
# name = "Clark"
# print(f"{name} is a programmer")

# list()
# split and join

# replace


# my_string = "hello world"
# for idx, ch in enumerate(my_string):
#     print(idx, ch)

# my_string = "hello world"
# for idx, ch in zip(range(len(my_string)), my_string):
#     print(idx, ch)


########################################## """
# """ un/comment to de/activate ################



########################################## """
# """ un/comment to de/activate ################



########################################## """
# """ un/comment to de/activate ################



########################################## """
# """ un/comment to de/activate ################



########################################## """
# """ un/comment to de/activate ################



########################################## """
