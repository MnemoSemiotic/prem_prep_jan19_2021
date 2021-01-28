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


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes) cont’d on next slide
Write a function that takes in a string. Return a dictionary where the keys represent unique characters in the string and the values represent the number of times that character appears in the original string. 
s = 'This is a string, we want you to count how many times each unique character appears in this string!'

Docstring and starter code:

```python
def num_chars(s):
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
    pass
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def clean_string(string):
    new_string = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for letter in string.lower():
        if letter in alpha or letter = ' ':
            new_string += letter
    return new_string

def word_letter_count(string):
    d = dict()
    cleaned = clean_string(string)
    word_list = cleaned.split(' ')

    for word in word_list:
        d[word] = len(word)

    return d
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `zip()`
You know how to iterate over a single data structure, but what if you have parallel lists? How can we iterate over these at the same time?
Syntax: 

```python
for i, j in zip(lst1, lst2):
	#some code here
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes) 
Write a function that prompts the user to input numbers separated by commas. Your script will then take these inputted numbers and store them as a list of tuples, two at a time. Use the zip() function to do this.  If the user inputs an odd number of numbers, then only make a list of the largest number of pairs of two that are possible.

Example: If you inputted the numbers `'1, 2, 3, 4, 5, 6'`, your function should return `[(1, 2), (3, 4), (5, 6)]`. If you inputted the numbers `1, 2, 3, 4, 5`, your function should return `[(1, 2), (3, 4)]`.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def build_tups():
    inp = input('Enter numbers, separated by commas: ')
    lst1 = []
    lst2 = []

    nums_str = inp.split(', ')

    for i in range(0, len(nums_str), 2):
        lst1.append(int(nums_str[i]))
        if i+1 < len(nums_str):
            lst2.append(int(nums_str[i+1]))

    return list(zip(lst1, lst2))

print(build_tups())
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# List Comprehensions

```python
new_lst = []
for i in old_lst:
    new_lst.append(i**2)

new_lst = [ i ** 2 for i in old_lst ]
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# List Comprehension w/ if statement

```python
new_lst = []
for i in old_lst:
	if i > 10:
        new_lst.append(i**2)

new_lst = [i ** 2 for i in old_lst if i > 10]
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# List Comprehension w/ if else statement

```python
new_lst = []
for i in old_lst:
	if i > 10:
        new_lst.append(i**2)
    else:
	    new_lst.append(i//2)

new_lst = [i ** 2 if i > 10 else i//2 for i in old_lst]
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `dict` Comprehension

```python
new_dict = {}
for i in old_lst:
	new_dict[i] = i**2

new_dict = {i:i**2 for i in old_lst}
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Generalization of comprehensions

```python
[f(x) for x in sequence]

[f(x) for x in sequence if condition]

[f(x) if condition else g(x) for x in sequence]

{key:value for x in sequence}
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
Let’s warm up with something easy:

Write a function that will calculate the total amount of a dinner bill, given the total before tax, the tax rate, and percentage. Your function will accept these three values as arguments. It will then do the following:
* Apply the tax rate to the bill total
* Apply the tip percentage to the total amount
* Return the total amount of bill before and after tip.

Here’s an example of how you would call the function:

```python
bill_with_tax, bill_with_tax_and_tip = calc_total_bill(100, 0.10, 0.10)
bill_with_tax_and_tip

>>> 121.0
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def calc_total_bill(bill, tax, tip):
    bill_and_tax = bill * (1+tax)
    tax_and_tip = bill * (1+tax) * (1+tip)
    return bill_and_tax, tax_and_tip
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (7 minutes)
1. Write a list comprehension of this list to get the len of each item, if an item doesn't have a len, make sure to change that item to a string before you take len.
    * `L1 = ['hello', 'goodbye', [1,2,3], 44]`

2. Write a list comprehension that takes in a list of positive integers and adds 100 to a single digit number else it will subtract 100 from the number.
    * `L2  = [1, 5, 8, 100, 43, 254, 1000, 3, 0, 88888]`

3. Write a dictionary comprehension of a dictionary, making the values the keys and the keys the values
    * `D1 = {'Apple':5, 'Pear': 10, 'Banana':2, 'Orange': 1}`

4. Write a dictionary comprehension of a dictionary, adding '_test' to the keys and finding the remainder of the value when divided by 13
    * `D2 = {'a': 540, 'b': 222, 'c':88, 'd':1000,'e':13}`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
1.

```python
L1 = ['hello', 'goodbye', [1,2,3], 44]
l1 = [len(item) if not isinstance(item, (int, float, complex, bool)) else len(str(item)) for item in L1]
```

2.

```python
L2  = [1, 5, 8, 100, 43, 254, 1000, 3, 0, 88888]
l2 = [n + 100 if abs(n / 10) < 1 else n - 100 for n in L2>]
```

3.

```python
D1 = {'Apple':5, 'Pear': 10, 'Banana':2, 'Orange': 1}
d1 = {v: k for k, v in D1.items()}
```

4.

```python
D2 = {'a': 540, 'b': 222, 'c':88, 'd':1000,'e':13}
d2 = {k+'_test': v%13 for k, v in D2.items()}
```
