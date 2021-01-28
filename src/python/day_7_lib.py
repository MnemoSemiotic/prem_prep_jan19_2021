""" un/comment to de/activate ################
# strings
# list()
# my_string = "Hello, world!"
# print(my_string)
# lst_of_chars = list(my_string)
# print(my_string)
# print(lst_of_chars)

# split and join
text = '''
Whose woods these are I think I know
His house is in the village though
He will not see me stopping here
To watch his woods fill up with snow
'''

# my_lst = text.split() # -> list
# print( text )
# print( my_lst )

# my_string = " ".join(my_lst)
# print(my_string)


# print(dir(""))
# help( "".zfill )

########################################## """
""" un/comment to de/activate ################

text = '''
Whose woods these are I think I know
His house is in the village though
He will not see me stopping here
To watch his woods fill up with snow
'''.lower()

# replace
print( text.replace("i", "you") )
print( text )


########################################## """
""" un/comment to de/activate ################

'''
Create a function that takes in a string. This function should split the string into a list of lowercase words that make up that string. Return a list of unique ‘cleaned’ words.

Challenge: strip any punctuation (for now, strip commas and periods)
Challenge: remove the common english words from the list below you are returning
'''
def clean_string_lst(txt_in):
    punct_lst = [",", ".", ";", ":", "!", "?", "'", '"'],
    remove_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "can", "will", "just", "don", "should", "now"]

    for punct in punct_lst:
        if punct in txt_in:
            txt_in = txt_in.replace(punct, "")

    lst = []
    for word in txt_in.lower().split():
        if word not in lst + remove_words:
            lst.append(word)

    return " ".join(lst)


my_txt = "Hello there! How are you? Why don’t you take a seat over there? Once we went to the store and we found ourselves in a strange place. We ran into two people. They were very interesting to talk to. Each of them had an interesting accent and we wondered where they were from."

print( clean_string_lst(my_txt) )
# print(my_txt)

########################################## """
""" un/comment to de/activate ################
# print(dir(tuple)) # 'count', 'index'


########################################## """
""" un/comment to de/activate ################

# lst = ["hey", "hello", "hi", "yo"]
dc1 = { "greeting_1": "hey" ,
        "greeting_2": "hello" ,
        "greeting_3": "hi" ,
         }

dc2 = { "greeting_1": "hey" ,
        "greeting_3": "hi" ,
        "greeting_2": "hello" ,
         }

ls1 = ["hey", "hello", "hi", "yo"]
ls2 = ["hey", "hello", "yo", "hi"]

print( ls1 == ls2 )
print( dc1 == dc2 )
print( lst[1]            )
print( dct["greeting_2"] )

########################################## """
""" un/comment to de/activate ################

# CRUD
# C
car_d = {}
car_d["year"] = 1983
car_d["make"] = "Toyota"
car_d["model"] = "Huntsman"
# car_d_year = 1983
# car_d_make = "Toyota"
# car_d_model = "Huntsman"
# car_d_model = "Civic"


# R
# print(car_d)
# print( car_d["year"] )
# print( type(car_d["year"]) )

# U
car_d["model"] = []
car_d["model"].append("Huntsman")
car_d["model"].append("Civic")
# print( car_d )



# D
# del d
del car_d["year"]
print(car_d)


########################################## """
""" un/comment to de/activate ################

my_set1 = set([4, 4, 6, 3, 5, 1, 5])
my_set2 = set([4, 9, 3, 1, 0, 1, 5])
print( my_set1 - my_set2 )
print( my_set2 - my_set1 )
print( my_set1.difference(my_set2) )
print( my_set2.difference(my_set1) )
print( my_set1.union(my_set2) )
print( my_set1.intersection(my_set2) )

########################################## """
""" un/comment to de/activate ################

# CRUD
# C
car_d          = {}
car_d["year"]  = 1983
car_d["make"]  = "Toyota"
car_d["model"] = "fancy car"
car_d["model"] = "Huntsman Civic"
print( car_d )
print( car_d["model"] )

# R
# print(car_d)
# print( car_d["year"] )
# print( type(car_d["year"]) )

# U
# car_d["model"] = []
# car_d["model"].append("Huntsman")
# car_d["model"].append("Civic")
# print( car_d )

# D
# del d
# del car_d["year"]
# print(car_d)

########################################## """
# """ un/comment to de/activate ################


names_lst = ["Jen", "Joe", "Jessie", "Jill"]
ages_lst  = [33, 44, 55]
for name, age in zip(names_lst, ages_lst):
    print(f"{name} is {age}")


# a, b = (4, 5)
'''
Zip makes an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

The iterator stops when the shortest input iterable is exhausted.

With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator
'''











########################################## """
# """ un/comment to de/activate ################



########################################## """
