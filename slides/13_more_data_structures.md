https://docs.google.com/presentation/d/1dZWsoak_vsQm0jWhU6rncxSvBohh4MITZ_K5gKpW5O0/edit#slide=id.p


# Data Structures Review
* Sets
* Tuples
* Dictionaries
* List, Dict, if/else comprehension






<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Review: Sets
* Sets are unordered, mutable collections
* Sets will only contain unique elements
* Sets can be declared:
    * Using the set constructor `set()`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)

```python
str1 = set('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.'.lower().replace('.', '').split(' '))
str2 = set('Complex is better than complicated. Flat is better than nested. Sparse is better than dense.'.lower().replace('.', '').split(' '))
```

* What is the intersection of str1 and str2?
* What is the union of str1 and str2?
* What is the difference of str1 - str2?

NOTE: Consider "cleaning" the string from punctuation. Also consider lower-casing.

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
* What is the intersection of str1 and str2?

```python
{'is', 'better', 'than'}
```

* What is the union of str1 and str2?

```python
{'better', 'implicit', 'complex', 'nested', 'dense', 'beautiful', 'complicated', 'complex', 'explicit', 'than', 'sparse', 'is', 'simple', 'flat', 'ugly'}
```

* What is the difference of str1 - str2?

```python
{'implicit', 'explicit', 'beautiful', 'complex', 'simple', 'ugly'}
```

* What is the difference of str2 - str1?

```python
{'dense', 'sparse', 'complex', 'nested', 'complicated', 'flat'}
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Review: Tuples
* Tuples are ordered collections 
* Tuples are very similar to lists with two key differences:
    * Tuples are immutable.
    * Tuples are declared using parenthesis.
* We can index and slice tuples because they are ordered
* Tuples have two methods associated with them: count and index
* Functions return tuples when returning more than one item


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Review: What is a Dictionary?
* Dictionaries contain key/value pairs in a mutable, unordered collection.
* Keys must be immutable and unique.
* Dictionaries are declared:
    * Using curly braces `{}`
* Syntax: `{key1 : value1, key2: value2, key3 : value3}`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
Write a function that prompts the user to input numbers separated by dashes ( - ). Your script will take those numbers, and print a dictionary where the keys are the inputted numbers, and the values are the squares of those numbers.

Example: If you inputted the numbers `‘1 - 5 - 8 - 10’`, your script should print `{8: 64, 1: 1, 10: 100, 5: 25}` (remember that dictionaries are unordered, which is why the script might print out the key-value pairs in a different order than the user inputted the numbers).


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def square_dict():
    inp = input('Enter numbers separated by dashes: ')
    inp_list = inp.split(' - ')
    d = {}
    for num in inp_list:
        d[int(num)] = int(num)**2
    return d
```