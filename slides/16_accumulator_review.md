# Review: f-strings, `.format()` and Accumulators
* String Formatting
    * f-strings
    * `.format()`
* Accumulator Review!
* String Accumulators
* List Accumulators
* Dictionary Accumulators


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# f-strings
* Your go-to for string interpolation
* Curly braces contain variable reference, operations, function calls, etc

```python
var1, var2 = 2, 3

print(f'{var1} out of {var2} programmers prefer f-strings')
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `.format()`
* You may still see and use this, but f-strings are generally preferable.
* Interpolates values into strings using the `.format()` method

```python
var1, var2 = 1, 3

print('{} out of {} programmers prefer the format method'.format(var1, var2))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Accumulators
* An accumulator can be thought of as a running total that is held in a variable	
* Accumulator Pattern: 

```
Initialize the accumulator variable
Repeat:
    Modify the accumulator variable
```

* When the above loop terminates, the accumulator will have the correct value. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Sum accumulators using `int` or `float`

* We can calculate a sum by using an numeric typed accumulator

```python
num = 0
for x in list_of_numbers:
	num += x
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Write a function called `accum_nums` that takes in an integer `n` as an argument it should perform the tasks below for a range of numbers from `1` through `n` (int accumulator starts at 1)
* If the number is divisible by 3, add 3 to the accumulator
* If the number is divisible by 5, divide accumulator by 5
* If number is divisible by 4, multiply the accumulator by 4
* If number is divisible by 3, 4, and 5 do nothing
* If number is divisible by 3 and 4, subtract 12 from accumulator
* If number is divisible by 3 and 5, floor divide accumulator by 15
* If number is divisible by 4 and 5, modulo accumulator by 20



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def accum_nums(n): 
    acc = 1
    for num in range(1, n+1): 
        if num % 4 == 0 and num % 5 == 0 and num % 3 == 0: 
            continue 
        if num % 4 == 0 and num % 3 == 0: 
            acc -= 12 
        if num % 3 == 0 and num % 5 == 0: 
            acc //= 15 
        if num % 4 == 0 and num % 5 == 0: 
            acc %= 20 
        if num % 3 == 0: 
           acc += 3 
        if num % 4 == 0: 
            acc *= 4 
        if num % 5 == 0: 
            acc /=5
    return acc 
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Accumulators using a `string`
* We can concatenate a string by using a `string` type accumulator

```python
str1 = ''
for s in string:
    str1 += s
```

* We can concatenate the string by letter, by word, or by some other separator within our string


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Write a function called `build_non_vowel_str()` that takes in a string and returns a string accumulator that accumulates all non-vowels.

Pass in this string:

```python
string = "It’s a beautiful day in the neighborhood, A beautiful day for a neighbor, could you be mine? Would you be mine?"
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def non_val(s):
	new_s = ''
	for char in s:
		if char.lower() in ['a', 'e', 'i', 'o', 'u']:
			continue
		else:
			new_s += char
    return new_s
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Write a function called `collect_evens()` that takes a list of integers. The function should return a string that accumulates the even numbers into a string.
* Example: `collect_evens([1, 2, 3, 4])` -> `'24'`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def collect_evens(lst):
	s = ''
	for i in l:
		if i % 2 == 0:
			s += str(i)
	return s
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
	# ...some code...
	accumulator.append(some_value)
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Write a function called `words_start_with()` with two parameters, a list of letters and a string. The function should return a new list filled with words from the string that start with the letters in the list of letters.
Test with this string:

```python
str1 = "It's a beautiful day in the neighborhood, A beautiful day for a neighbor, could you be mine? Would you be mine?"
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)

```python
def words_start_with(letters, string): 
    lst = []
    for word in string.split(): 
        if word[0].lower() in letters: 
            lst.append(word) 
    return lst
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Write a function called `examine_lst()` that takes a list of various values as an argument, then returns a new list of those values processed by these rules:
* Accumulate elements that are not integers
    * If an element is a float, change it to a string
    * If an element is a string, get the length of that string
* Test String:

```python
l1 = [192, 504, 23.11, 3.14, 'table', 'chair', 55, 1039.1, 0, 0.0, '0.0', 'python']
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def examine_lst(l): 
    out_l = [] 
    for i in l: 
       if type(i) == float: 
            out_l.append(str(i)) 
       elif type(i) == str: 
            out_l.append(len(i))
		 elif type(i) != int:
    out_l.append(i) 
    return out_l
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators
* Sometimes, you will need an accumulator that is an dictionary.
* The accumulator either create a new key value pair or it will add something to the value of an already existing key value pair. 
* Syntax for a dictionary counter: 

```python
accumulator = {}
for element in some_list:
	if element in accumulator.keys():
		accumulator[element] += 1
	else:
		accumulator[element] = 1
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along ...
Write a function that will:
* For any given string, return a dictionary that gives us the number of vowels, the number of non vowels, the number of non-alpha characters.

## Let’s do this together!


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along ...


**Step 1:**
We need to first create a dictionary that we can store all our information in.

```python
d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0}      
```

We can fill our dictionary like this because we know exactly what the question is asking and because we want counts, we can use integer accumulators for our values using addition.

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along ...

**Step 2:**

```python
d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0}     
```

We now need to iterate over our string and identify each of the three types of characters we are interested.

How can we identify vowels in a string?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along ...

**Step 2:**

```python
d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0}     
```

We now need to iterate over our string and identify each of the three types of characters we are interested.

How can we identify vowels in a string?

```python
if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    # do something
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along ...

**Step 2:**

```python
d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0}     
```

We now need to iterate over our string and identify each of the three types of characters we are interested.

How can we identify non-alphas in a string?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along ...

**Step 2:**

```python
d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0}     
```

We now need to iterate over our string and identify each of the three types of characters we are interested.

How can we identify non-alphas in a string?

```python
elif not char.isalpha():
    # do something
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along ...

**Step 2:**

```python
d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0}     
```

We now need to iterate over our string and identify each of the three types of characters we are interested in.

Based on this, we can use just a regular else statement to cover all other characters


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along ...

**Step 2:**

```python
d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0}     
``` 

Let’s put it all together - you now fill in the blanks of how to use our dictionary to accumulate here

```python
if char in ['a', 'e', 'i', 'o', 'u']:
	pass
elif not char.isalpha():
	pass
else:
	pass
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along END

**Step 2:**

```python
d = {'vowels': 0, 'consonants': 0, 'nonalpha': 0}     
```

Let’s put it all together - you now fill in the blanks of how to use our dictionary to accumulate here

```python
if char in ['a', 'e', 'i', 'o', 'u']:
	d['vowels'] += 1
elif not char.isalpha():
	d['nonalpha'] += 1 
else:
	d['consonants'] += 1
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
Write a function that take in an integer and will roll a 6-sided dice randomly for that number of times and will update the proportions of each number occurring and update the counts also 
* Have your function return:
    * A dictionary of counts
    * A dictionary of dice proportions


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
What is the first thing we need to do?
Assume we have already 

```python
import random
```

What do we need to create?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
What is the first thing we need to do?
Assume we have already 

```python
import random
```

What do we need to create?

```python
counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
probs = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total_rolls = 0
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
What is the first thing we need to do?
Assume we have already 

```python
import random
```

Now we can iterate over our integer we called in our function and call `random.randint(1,6)` which will return a number randomly 1-6

Based on what that roll is we can update our count dictionary and probability dictionary


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
What is the first thing we need to do?
Assume we have already 

```python
import random
```

Now we can iterate over our integer we called in our function and call `random.randint(1,6)` which will return a number randomly 1-6

Based on what that roll is we can update our count dictionary and probability dictionary

```python
roll = random.randint(1, 6)
counts[roll] += 1
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
What is the first thing we need to do?
Assume we have already 

```python
import random
```

Now we can iterate over our integer we called in our function and call `random.randint(1,6)` which will return a number randomly 1-6

Based on what that roll is we can update our count dictionary and probability dictionary.

How do we update the probability dictionary?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
Well we know we need to update every value in our probs dictionary, what does that lead you to want to use when we think about iterating over a dictionary?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
Well we know we need to update every value in our probs dictionary, what does that lead you to want to use when we think about iterating over a dictionary?

```python
for k, v in probs.items():
```

So now how do we update our probs where the numerator will be updated for the value that the dice rolled and the denominators will be updated for all of our key:value pairs?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...
Well we know we need to update every value in our probs dictionary, what does that lead you to want to use when we think about iterating over a dictionary?

```python
for k, v in probs.items():
	probs[k] = counts[k]/total_rolls
```

We have parallel dictionaries (like parallel lists) so our keys can be used to access values from both dictionaries!


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Dictionary Accumulators Code Along #2 ...

#### Let’s say we rolled a `5` after rolling a `1`

```python
roll = random.randint(1, 6)
       counts[roll] += 1
       total_rolls += 1
counts = {1: 1, 2: 0, 3: 0, 4: 0, 5: 1, 6: 0}
total_rolls += 1
for k, v in probs.items():
	probs[k] = counts[k]/total_rolls
probs = {1: 1/2, 2: 0/2, 3: 0/2, 4: 0/2, 5: 1/2, 6: 0/2}
```