# Loops
* Traversing a `list`
* accumulators
* boolean flags
* `list` accumulators
* loops as filters
* break
* continue
* pass


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, [“hello”, 85, True], 0]
```

* How would you index to get the value `8`
* How would you slice to get the `list`: `[5, 3, 1]`
* How would you replace the value `4` with the value `10` using indexing?
* How would you slice into the `list` to get: `["hello", 85]`
* How would you add the value `42` to the `list`?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, [“hello”, 85, True], 0]
```

* How would you index to get the value `8`
    * `print(x[7])`
* How would you slice to get the `list`: `[5, 3, 1]`
    * `print(x[4::-2])`
* How would you replace the value `4` with the value `10` using indexing?
    * `x[3] = 10`
* How would you slice into the `list` to get: `["hello", 85]`
    * `print(x[9][:2])`
* How would you add the value `42` to the `list`?
    * `x.append(42)`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `for` loops
* For loops iterate through each element of a `list`
    * Syntax: 

```python    
for element in list:
	print(element)
```

* Another way to use a `for` loop is to iterate through `range(len(list))` in order to access all the indices, rather than the elements themselves. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Traversing a `list`
* What actually happens when we go through each iteration of a loop?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (6 minutes)
Given the following `list` of letters, create a function that goes through each letter and prints the letter if it is a vowel.

```python
char_list = ['o', 'r', 'c', 'h', 'i', 'd']
```

* It will be helpful to write a helper function that returns True if a character is a vowel and call it within this function
* Create a plan before coding


<br><br><br><br><br><br><br><br><br>

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


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (6 minutes)
Given two arbitrary lists, write a function that finds the common elements between them. Store these common elements in a `list`, and return that `list`

* Bonus 1: return the items sorted in the returned `list`
* Bonus 2: make sure there are no duplicates in the returned `list`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def get_common_elements(lst1, lst2):
    output = []

    for item in lst1:
        if item in lst2:
            if item not in output:
                output.append(item)
    
    return sorted(output)

lst_a = [4,9,6,5,7,8,6,2]
lst_b = [1,2,3,4,5,6,7]

print(get_common_elements(lst_a, lst_b))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Accumulators (are important!)
* An accumulator can be thought of as a running total that is held in a variable	
* Accumulator Pattern: 
    * Initialize the accumulator variable
    * Repeat:
        * Modify the accumulator variable
    * When the above loop terminates, the accumulator will have the correct value. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Sum accumulators using an `int`
* We can calculate a sum by using an integer type accumulator
summ = 0

```python
for num in nums:
	summ += num
```

* We can also calculate the sum when our list is comprised of floats. 
* The final accumulator will be a float. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Boolean Flags 
* Occasionally, you will need to use an accumulator that is set to a boolean value. 
* If some condition is met in the for loop, the boolean assigned to the accumulator will change to the opposite value. Otherwise, it will stay the same.
* These boolean flags can also be used as exit conditions in a loop.
* Syntax:   

```python
accumulator = False
for element in some_list:
    # some code
    if some_condition:
        accumulator = True
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `is_prime()` function ...
* Let’s code it using a boolean flag


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `is_prime()` function

```python
def is_prime(num):
    prime = True
    if num == 2 or num == 3:
        return True

    for divisor in range(2, num):
        if num % divisor == 0:
        prime = False
    
    return prime

for i in range(2, 100):
    print(i, is_prime(i))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `list` Accumulators
* Sometimes, you will need an accumulator that is an empty list.
* As the for loop gets evaluated, the accumulator will be appended with new values. 
* Syntax: 

```python
accumulator = [ ]
for element in some_list:
    # some code
    accumulator.append(some_value)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Using loops as filters
* We can filter list elements that meet a condition using accumulators.
* As the for loop is evaluated, values that meet the condition will be appended to a new empty list. 
* Syntax: 

```python
some_list = [stuff, more stuff]
accumulator = [ ]
for element in some_list:
    if some_condition:
        accumulator.append(element)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `break`
* Use `break` in `for` loops to exit the loop when some condition has been met
* Syntax:

```python
for element in some_list:
if some_condition:
	break
```

* Use `break` in `while` loops to avoid an infinite loop


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Using `break` in `is_prime()`
* Use break to exit the loop

```python
def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break # this will end early
    return prime
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `continue`

* Use `continue` in `for` loops in order to skip code and continue to the next iteration of the loop when some condition is met
* Syntax:

```python
for element in some_list:
    if some_condition:
	    continue
    # some code
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# pass
* Use pass as a placeholder for future code
* Syntax:

```python
for element in some_list:
    pass

def function_name():
	pass
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
* Write a function to calculate the result of n!

$$
4! = 4 * 3 * 2 * 1
$$

$$
3! = 3*2*1
$$

$$
0! = 1
$$

* Think about edge cases 



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def factorial(num):
    prod = 1
    if num == 0:
        return prod
    if num < 0:
        print('Negative factorial is undefined')

    for i in range(num+1):
        prod *= i

    return prod
```



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
* Write a function to sum all even numbers in a `list`


# BREAKOUT SOLUTION

```python
def sum_evens(num_list):
    accum = 0

    for num in num_list:
        if num % 2 == 0:
            accum += num
    return accum
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------