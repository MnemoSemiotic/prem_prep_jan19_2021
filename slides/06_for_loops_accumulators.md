# Loops
* Traversing a list
* accumulators
* boolean flags
* list accumulators
* loops as filters
* break
* continue
* pass

---------------------------------------------------------------
# BREAKOUT (3 minutes)
```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, [“hello”, 85, True], 0]
```

* How would you index to get the value `8`
* How would you slice to get the list: `[5, 3, 1]`
* How would you replace the value `4` with the value `10` using indexing?
* How would you slice into the list to get: `["hello", 85]`
* How would you add the value `42` to the list?

---------------------------------------------------------------
# BREAKOUT SOLUTION
```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, [“hello”, 85, True], 0]
```

* How would you index to get the value `8`
    * `print(x[7])`
* How would you slice to get the list: `[5, 3, 1]`
    * `print(x[4::-2])`
* How would you replace the value `4` with the value `10` using indexing?
    * `x[3] = 10`
* How would you slice into the list to get: `["hello", 85]`
    * `print(x[9][:2])`
* How would you add the value `42` to the list?
    * `x.append(42)`

---------------------------------------------------------------
# `for` loops
* For loops iterate through each element of a list
    * Syntax: 

```python    
for element in list:
	print(element)
```

* Another way to use a `for` loop is to iterate through `range(len(list))` in order to access all the indices, rather than the elements themselves. 

---------------------------------------------------------------
# Traversing a `list`
* What actually happens when we go through each iteration of a loop?

---------------------------------------------------------------
# BREAKOUT (6 minutes)
Given the following list of letters, create a function that goes through each letter and prints the letter if it is a vowel.

```python
char_list = ['o', 'r', 'c', 'h', 'i', 'd']
```

* It will be helpful to write a helper function that returns True if a character is a vowel and call it within this function
* Create a plan before coding

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
char_list = ['o', 'r', 'c', 'h', 'i', 'd']

def is_vowel(let):
    if let in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

def print_vowels(lst):
    for char in lst:
        if is_vowel(char):
            print(char)

print_vowels(char_list)
```

---------------------------------------------------------------
