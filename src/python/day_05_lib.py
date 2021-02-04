""" un/comment to de/activate ################

lst = [5, 6, 4, 2, 3, 9, 4, 8]
print(lst[1:5+1:])

########################################## """
""" un/comment to de/activate ################

lst = [4, 5, 9, 3, "hello", [9, 0, 1, "hi", 4], 5, 6]
print( lst[5][1:3+1:] )

########################################## """
""" un/comment to de/activate ################

# mutability -> means the value can change but the object is the same object

# immutable value changes the id changes
# x = 7
# print( x, id(x) )
# x = x + 1
# print( x, id(x) )


# mutable if the value changes the id does not change
# lst = []
# print( lst, id(lst) )
# lst = lst.append(42)
# print( lst, id(lst) )


# x = 3
# x = x + 1

########################################## """
""" un/comment to de/activate ################

def remove_greater_than_10(num_lst):
    out_lst = num_lst.copy()
    for el in num_lst[::]:
        if el > 10:
            out_lst.remove(el)

    return out_lst


my_lst = [5, 6, 12, 83, 4, 77, 2349857]
print( remove_greater_than_10(my_lst) )
print( my_lst )
# [5, 6, 4]

########################################## """
# """ un/comment to de/activate ################
# num1, num2, num3 = [5, 6, 4]
# a, b = 1, 3
# print(num3, num2, num1)

########################################## """
""" un/comment to de/activate ################

def square_nums_lst(in_lst):
    lst = []
    for num in in_lst:
        if num > 4:
            lst.append(num**2)

    return lst


data_lst = [5, 6, 4, 2, 3, 9, 4, 8]
print(square_nums_lst(data_lst))
print(data_lst)

########################################## """
""" un/comment to de/activate ################

def vowels_lst(seq):
    lst = []
    for c in seq:
        if c.lower() in "aeiou":
            lst.append(c)

    return lst


char_list = ['o', 'r', 'c', 'h', 'i', 'd']
print(vowels_lst(char_list))


########################################## """
""" un/comment to de/activate ################
def common_elements(lst1, lst2):
    lst = []
    for el in lst1:
        if el in lst2 and el not in lst:
            lst.append(el)

    return sorted(lst)


my_lst1 = [3, 6, 1, 8, 6, 0, 8]
my_lst2 = [2, 9, 8, 9, 6]
print(common_elements(my_lst1, my_lst2))
########################################## """
""" un/comment to de/activate ################

def sum_of_squares(num_lst):
    total = 0 # target
    for num in num_lst:
        total += num**2

    return total


my_lst = [5, 8, 9, 8, 2]
print(sum_of_squares(my_lst))

########################################## """
""" un/comment to de/activate ################

n = 95
flag = False
for i in range(10):
    if i + n > 100:
        flag = True

print(flag)

########################################## """
""" un/comment to de/activate ################

my_lst = [5, 8, 3, 5, 2, 8, 9, 8, 2]

prev_num = None
flag = False
for num in my_lst:
    if flag:
        flag = False
        print(num**prev_num)
    if num <= 3:
        flag = True
        prev_num = num

########################################## """
""" un/comment to de/activate ################

def is_prime(n):
    prime = True
    if n < 2:
        prime = False

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    return prime


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for i in range(16):
    print(i, is_prime(i)) # False

########################################## """
