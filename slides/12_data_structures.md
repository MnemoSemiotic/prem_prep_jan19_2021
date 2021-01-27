# Data Structures
* Sets
* Tuples
* Dictionaries


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `set()` datatype
* Sets are unordered, mutable collections
* Sets will only contain unique elements
* Sets can be declared:
    * Using the set constructor `set()`
* Be careful when declaring empty sets. `{}` defaults to dictionaries.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Removing Duplicates
* Sets only hold unique elements. 
    * This property is useful for removing duplicates from lists and tuples
    * Do this by casting the `list` or `tuple` to a `set`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Union and Intersection
* The union and intersection methods in sets are similar to their mathematical analogues.
* The union is a set of all elements in two sets
    * Syntax: `set1.union(set2)`
* The intersection is a set of all the elements that two sets have in common
Syntax: `set1.intersection(set2)`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Set Difference
* The difference of two sets A - B contains all the elements of set A that are not contained in set B
* Syntax: `set1.difference(set2)`
* `set1.difference(set2)` is different from  `set2.difference(set1)`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)

```python
l1 = [1, 4, 7, 0, 2, 5, 8]
l2 = [1, 2, 3, 4, 9]
```

* What does the intersection of these two lists return?
* What does the the union of these two lists return?
* What does the difference of `l1 - l2` return? 
* What about `l2 - l1`?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `tuple()` datatype
* Tuples are ordered collections 
* Tuples are very similar to list with two key differences:
    * Tuples are immutable.
    * Tuples are declared using parenthesis.
* We can index and slice tuples because they are ordered
* Tuples have two methods associated with them: count and index


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Declaring Tuples 
* Tuples can be declared in three ways:
    * `tup = (1, 2, 3)`
    * `tup = tuple([1, 2, 3])`
    * `tup = 1, 2, 3`
* For single elements tuples:
    * `tup = (1,)`
    * `tup = tuple([1])`
    * `tup = 1,`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Tuple Immutability
* Once a tuple is declared, it generally can’t be changed in anyway
    * However, if an element of a tuple is mutable, the element can be changed
* Tuples hold references to all the objects they contain, rather than the objects themselves. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Write a function that has two arguments that are both tuples. Return a single tuple that is the combination of the two original tuples that skips every other element in reverse.
* Say `tuple1 = (12, 14, 16, 18)` and `tuple2 = (3, 5, 7, 9)`:
* The result would be `(9, 5, 18, 14)`

```python
def function_name(tuple1, tuple2):
   pass
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python



```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionaries
* Dictionaries contain key/value pairs in a mutable, unordered collection.
* Keys must be immutable and unique.
* Dictionaries are declared:
    * Using curly braces `{}`
    * `dict()` constructor
* Syntax: `{key1 : value1, key2: value2, key3 : value3}`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Accessing and Updating Key Value Pairs
* Access values by using the key as an index:
    * `d[key]`
    * This statement will throw an error if the key is not in the dictionary.
* Keys can be added to dictionaries by:
    * `d[new_key] = new_value`
    * Note that if the key already exists in the dictionary, this syntax will reassign the value to this new_value


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Methods
* The keys method will return a list of the keys in a dictionary
    * `dct.keys()`
* The values method will return a list of the values in a dictionary
    * `dct.values()`
* The items method will return a list of tuples that contain the key/ value pairs
    * `dct.items()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Membership
* Membership for dictionaries
    * `k in dct`
    * `k in dct.keys()`
    * `v in dct.values()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Traversing a Dictionary
* Creating a for loop allows us to iterate through a dictionary’s keys

```python
for key in dictionary:
    print(key)
```

* Combining a for loop with the items method allows us to iterate through both the keys and the values of a dictionary:

```python
for key, value in dictionary.items():
    print(key, value)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Deleting Key/Value Pairs
* In order to remove key/value pairs, you can use the pop method or the del keyword
    * `d.pop('some_key')`
    * `del d['some_key']`
* Create a copy of the original dictionary before changing it by adding and deleting key/value pairs
    * `dictionary.copy()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `.get()`
* To check and see if a specific key is in a dictionary, you can use the get method
    * Syntax: `dct.get(key, default=None)`

```python
states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}
d.get(‘Washington’, ‘Capital not found’)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Copying a dictionary

To make a copy of a dictionary you need to use the `.copy()` method
* Syntax: `dct.copy()`
* Err on the side of making copies of dictionaries