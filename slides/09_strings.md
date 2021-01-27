# Strings
* Declaring `strings`
* `string` methods
* Functions with `strings`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `string` datatype
* Strings are simply a collection of characters
* However, in Python, a `string` is a scalar type and is immutable
* Strings are declared with single, double, or triple quotes. 
    * Mostly interchangeable. Single and double quotes only work with strings that span one line. 
    * Strings that span multiple lines need to be declared using triple quotes.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Basic `string` Operators 
* We can use the addition operator to concatenate strings.
    * `'My first string ' + 'My second string'` => `'My first stringMy second string'`
* The multiplication operator will repeat the string `n` times. 
    * `'Repeating string' * 3` => `'Repeating stringRepeating stringRepeating string'`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Casting to and from a `string`
* Just about any data type can be cast to a `string`.
    * Use the `string` casting function: `str()`
* Not every `string` can be cast to another data type.
    * `int('a')` will not work
* String concatenation will only work between strings
    * Need to cast any numeric variables to a `string` before concatenating. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Join a `list` to create a `string`
* Use the `join` `string` method to create a single `string` that contains all the elements of a `list`. 
    * `''.join(list)`
* All the elements of the `list` must be strings for the `join` method to work
    * You can use the `map` function to quickly cast all the elements of a `list` to strings 
    * `list(map(str, list))`



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `string` Slicing
* Use slice indexing (similar to a list) to access characters or subsequences of characters
* `string[index]`
* `string[start:end]`
* `string[start:end:skip]`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `string` membership
* Check if a string is a substring of another string using the in keyword. 
    * `'str' in 'string'`
    * Returns a boolean


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `replace`
* The `replace` method is used to replace every occurence of a specified substring in the original substring with another substring
    * Syntax: `string.replace(old_substring, new_substring, 1)`
* The third argument here will limit the amount of times the `replace` method will be applied to only once.

```python
string = 'I love to look at the moon'

string = string.replace('o', 'puppy', 2)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `enumerate`
* The `enumerate` function can be used on strings:

```python
for idx, ch in enumerate(string):
    print(idx, ch)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
Write a function that takes a `list` like the following `list` of column names and change any spaces in the column names to underscores. Return a modified `list` with the updated names.

```python
column_names = ['gender', 'longest absence from school', 'is enrolled', 'enlist', 'unemployed', 'filed for bankruptcy', 'school', 'peace corps']
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
column_names = ['gender', 'longest absence from school', 'is enrolled', 'enlist', 'unemployed', 'filed for bankruptcy', 'school', 'peace corps']

def add_underscores(feature_list):
    new_list = feature_list.copy()
    for idx, column in enumerate(new_list):
        if ' ' in column:
            new_list[idx] = column.replace(' ', '_')

    return new_list

```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `list()` Function
* A `string` can be cast to a `list` using the `list` function
    * `list(string)`
* The `list()` function will separate each character in the `string` into a new element in the returned list.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `split()` Method
* Quick aside: Strings are immutable so methods will not change the `string` in place like with lists. 
* This method splits a `string` at each occurrence of a specified delimiter and will return a list with each split substring.
    * `string.split(delimiter)`
* The delimiter will not be included in the returned `list`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `lower()`, `upper()`, `swapcase()`, and `capitalize()`
* The `lower` method will return a `string` where all the letters are lowercase
    * Syntax: `string.lower()`
* The `upper` method will return a `string` where all the letters are uppercase
    * Syntax: `string.upper()`
* The `swapcase` method will return a `string` where all the letter’s cases are swapped
    * Syntax: `string.swapcase()`
* The `capitalize` method will return a `string` where the first letter of the `string` will be capitalized and the rest will be lower case.
    * Syntax: `string.capitalize()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `string` Formatting
* The `format` method will dynamically insert the variables passed in as parameters into the placeholders in a `string`
    * Syntax: `'Inserting {} into this string'.format(variable_to_insert)`
* `f` strings will dynamically insert variables into strings. The difference is that we just need to place the variable name in the curly braces.
    * Syntax: `f'Inserting {variable_to_insert} into this string'`



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (8 minutes)
Write a function that takes in a string. Return two parallel lists: one that contains the unique characters in the string and another that has the number of times that character appears in the original string. 

```python
s = 'This is a string, we want you to count how many times each unique character appears in this string!'
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION Examples

```python
s = 'This is a string, we want you to count how many times each unique character appears in this string!'

def get_letter_count(string):
    letters = []
    counts = []

    for let1 in string:
        index = 0
        if let1 not in letters:
            letters.append(let1)
            counts.append(0)
            index = len(letters) - 1
        else:
            for idx, let2 in enumerate(letters):
                if let1 == let2:
                    index = idx
                    break
        counts[index] += 1
    return letters, counts

letters, counts = get_letter_count(s)

for i in range(len(letters)):
    print(f'{letters[i]}: {counts[i]}')
```

or

```python
s = 'This is a string, we want you to count how many times each unique character appears in this string!'

def get_letter_count(string):
    letters = []
    counts = []

    for let in string:
        if let not in letters:
            letters.append(let)
            counts.append(1)
        else:
            counts[letters.index(let)] += 1
    
    return letters, counts

letters, counts = get_letter_count(s)

for i in range(len(letters)):
    print(f'{letters[i]}: {counts[i]}')
```