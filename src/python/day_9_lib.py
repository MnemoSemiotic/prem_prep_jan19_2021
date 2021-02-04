""" un/comment to de/activate ################
# string formating
# f strings
# name = "Sally"
# age = 47
# print("Sally is 47")

def name_is_age(name, age):
    return f"{name} is {age}"
    # return "{} is {}".format(name, age)


user_input_name = input("name: ")
user_input_age  = input("age: ")
print( name_is_age(user_input_name, user_input_age) ) # "Bob is 59"
# print( name_is_age("Joe", 27) ) # "Bob is 59"

# the .format method

########################################## """
# """ un/comment to de/activate ################
# accumulators
# int, float
# acc = 0
# for i in range(20, 47):
#     if i % 7 == 0:
#         acc += 1 # accumulation
#
# print( acc ) # 4

# boolean flag

# str
# tuple
# list
# lst = []
# sum_squares = 0
# for i in range(10, 20):
#     lst.append(i**2) # action
#     sum_squares += i**2 # action
#
# print(lst)
# print(sum_squares)

# dict
    # empty dict
    # accumullating on the values only


########################################## """
""" un/comment to de/activate ################
'''
Write a function called `accum_nums` that takes in an integer `n` as an argument it should perform the tasks below for a range of numbers from `1` through `n` (including n)
(int accumulator starts at 1)

* If the number is divisible by 3, add 3 to the accumulator
* If the number is divisible by 5, divide accumulator by 5
* If number is divisible by 4, multiply the accumulator by 4
* If number is divisible by 3, 4, and 5 do nothing
* If number is divisible by 3 and 4, subtract 12 from accumulator
* If number is divisible by 3 and 5, floor divide accumulator by 15
* If number is divisible by 4 and 5, modulo accumulator by 20
'''
def accum_nums(n):
    acc = 1
    for num in range(1, n):
        if num % 3 == 0 and num % 4 == 0 and num % 5 == 0:
            continue
        if num % 3 == 0 and num % 4 == 0:
            acc -= 12
        if num % 3 == 0 and num % 5 == 0:
            acc //= 15
        if num % 4 == 0 and num % 5 == 0:
            acc %= 20
        if num % 3 == 0:
            acc += 3
        if num % 5 == 0:
            acc /= 5
        if num % 4 == 0:
            acc *= 4

    return acc

print(accum_nums(10))

########################################## """
""" un/comment to de/activate ################

def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i

    return prod

print(factorial(4439287)) # 24

########################################## """
""" un/comment to de/activate ################

def uncorrupted_text(txt):
    string = ""
    for c in txt:
        if not c.isdigit():
            string += c

    return string


print( uncorrupted_text("Hel5lo, wor2ld!") )

########################################## """
""" un/comment to de/activate ################

'''
Write a function called `build_non_vowel_str()` that takes in a string and returns a string accumulator that accumulates all non-vowels.

Pass in this string:

```python
string = "It’s a beautiful day in the neighborhood, A beautiful day for a neighbor, could you be mine? Would you be mine?"
```
'''
def build_non_vowel_str(txt):
    string = ""
    for c in txt:
        if c.lower() not in "aeiou":
            string += c

    return string


def build_non_vowel_str(txt):
    for v in "aeiouAEIOU":
        txt = txt.replace(v, "")

    return txt

my_string = "It’s a beautiful day in the neighborhood, A beautiful day for a neighbor, could you be mine? Would you be mine?"
print( build_non_vowel_str(my_string) )

########################################## """
""" un/comment to de/activate ################

'''
Write a function called `collect_evens()` that takes a list of integers. The function should return a string that accumulates the even numbers into a string.
'''
def collect_evens(lst):
    string = ""
    for num in lst:
        if num % 2 == 0:
            string += str(num)

    return string

print(collect_evens([1, 2, 3, 4])) # '24'

########################################## """
""" un/comment to de/activate ################

lst = []
for i in range(10, 20):
    lst.append(i**2)

print(lst)

########################################## """
""" un/comment to de/activate ################

'''
Write a function called `words_start_with()` with two parameters, a list of letters and a string. The function should return a new list filled with words from the string that start with the letters in the list of letters.
Test with this string:
'''
def words_start_with(lst_in, txt):
    lst = []
    for word in txt.split():
        for st in lst_in:
            if word.startswith(st):
                lst.append(word)
                break

    return lst

str1 = "It's a beautiful day in the neighborhood, A beautiful day for a neighbor, could you be mine? Would you be mine?"

print(words_start_with(["ne", 'c', "w", "be"], str1))

########################################## """
""" un/comment to de/activate ################

'''
Write a function called `examine_lst()` that takes a list of various values as an argument,

returns a new list of those values processed by these rules:
* Accumulate elements that are not integers
* If an element is a float, change it to a string
* If an element is a string, get the length of that string

'''
def examine_lst(lst_in):
    lst = []
    for elem in lst_in:
        if type(elem) == int:
            continue
        elif type(elem) == float:
            lst.append(str(elem))
        elif type(elem) == str:
            lst.append(len(elem))

    return lst

l1 = [192, 504, 23.11, 3.14, 'table', 'chair', 55, 1039.1, 0, 0.0, '0.0', 'python']

print( examine_lst(l1) )
########################################## """
""" un/comment to de/activate ################

accumulator = {}
for element in some_list:
	if element in accumulator.keys():
		accumulator[element] += 1
	else:
		accumulator[element] = 1

########################################## """
""" un/comment to de/activate ################

'''
For any given string,

return a dictionary that gives us
[_]the number of vowels,
[_]the number of non vowels,
[_]the number of non-alpha characters.
'''

def txt_analyzer_d(txt):
    d = { "vowels": 0 ,
          "non_vowels": 0 ,
          "non_alphas": 0
        }
    for ch in txt:
        if ch.lower() in "aeiou":
            d["vowels"] += 1
        else:
            d["non_vowels"] += 1
        if not ch.isalpha():
            d["non_alphas"] += 1

    return d


print(txt_analyzer_d("Hello there how are you?"))
# { "vowels": <int> , "non_vowels": <int>, "non_alphas", <int>(5) }

########################################## """
# """ un/comment to de/activate ################

# print( dir("") )
# help( "".isalpha )

########################################## """
# """ un/comment to de/activate ################



########################################## """
