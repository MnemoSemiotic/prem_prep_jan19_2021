# While loops:
* `while`
* infinite loop
* conditional loops
* open ended problems
* menus
* `for` vs `while` loops


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `while` loops
* Use `while` loops when the number of iterations needed to complete a loop is not known
* Syntax:

```python
while some_condition:
    some code
```

* Typically, `while` loops have some counter or flag as well. 

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Infinite `while` Loops
* What happens if we run the code below?
* Syntax:

```python
counter = 1
while counter < 10:
    print(‘testing’)
```

* Avoid writing infinite loops

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Using a `for` in place of a `while`
* A `for` loop can be set with an arbitrarily high ranged number and an escape condition
* Creates code safe from infinite loops

```python
for _ in range(10000000):
    # do something
    if condition_met:
        break
```

# Conditional `while` Loops
* Mostly `while` loops get initialized with some sort of conditional statement. The `while` loop will execute until the statement is no longer `True`
* Syntax:

```python
counter = 0
while some_condition:
    # some code
    # change counter
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
* Write a function that computes and returns a `list` of all of the divisors of some positive number. Use a `while` loop. Things to think about:
    * How do you determine if a single number is a divisor of another?
    * What is your stopping condition?
    * BONUS: rewrite this with a `for` loop

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
## `while` loop solution

```python
def get_divisors(number):
    divisors = []
    divisor = 1

    while divisor <= number:
        if number % divisor == 0:
            divisors.append(divisor)
        divisor += 1

    return divisors

print(get_divisors(144))
```

## `for` loop solution

```python
def get_divisors(number):
    divisors = []

    for divisor in range(1, number+1):
        if number % divisor == 0:
            divisors.append(divisor)

    return divisors

print(get_divisors(144))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Open-ended Problems
* An open-ended problem is one where we do not know how many iterations we will need in order to solve the problem
* For example:
    * Converging on $\pi$ through a random sampling process, you'll want an exit condition for when you reach a certain level of surety
    * Run state for an application, where "Quit" would be the only instance where the containing loop would exit.

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Menu Using a `while` Loop
* [Menu Example on Replit](https://repl.it/@gDSIprep/whileloopsmenuwhileusingaloop)

```python
selections = []
another_order = True

while another_order == True:
    menu_string = '''Select from this list:
    1 : bread
    2 : butter
    3 : potatoes
    4 : broccoli'''

    print(menu_string)

    inp = int(input('please make a selection, 1-4: '))

    if inp in [1,2,3,4]:
        selections.append(inp)
    else:
        print('-- your selection was not understood --')
        continue

    inp2 = input('would you like to place another order? (y/n)')

    if inp2 == 'y':
        continue
    else:
        another_order = False


print(f'Your order list: {selections}')
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `for` Loops vs. `while` Loops
* In general, always use `for` loops to avoid infinite loops
    * Will always terminate at the end of an iterable when traversing elements in that iterable
    * Useful when you know how many iterations are needed
* However, there are some problems that should be solved using `while` loops
    * Open-ended problems
    * Menus
    * Run States


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (2 minutes)
* Why would we use break in our code? What about continue and pass?
* Why might we use a while loop?
* What is the syntax for a while loop?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

* Why would we use break in our code? What about continue and pass?
    * Use break to end loopage that no longer needs to be performed
    * Use continue to avoid an operation within a loop
    * Use pass as a placeholder in loops, conditions (if, elif, else), functions and other places to avoid errors
* Why might we use a while loop?
    * You can pretty much always avoid using a while loop
    * You can use while loops for “open-ended problems”, where you don’t know how many iterations you will need to perform
* What is the syntax for a while loop?

```python
while condition:
    # Do something
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# List Review BREAKOUT (3 minutes)
```python
x = [4, 6, 1, 2, 8, 0]
```

* How would you sort your list to save it in place?
* How would you sort your list to return a printed output?
* How would you reverse your list to save it in place?
* What would any(x) return? all(x)?
* How would you remove the first element in the list and append it to the end? Can you write this in a single line of code?

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# List Review BREAKOUT (3 minutes)
```python
x = [4, 6, 1, 2, 8, 0]
print(x)
# * How would you sort your list to save it in place?
x.sort()
# or
x = sorted(x)

# * How would you sort your list to return a printed output?
print(sorted(x))

# * How would you reverse your list to save it in place?
x.reverse()
# or
x = x[::-1]
print(x)

# * What would any(x) return? all(x)?
print(any(x)) # True
print(all(x)) # False

# * How would you remove the first element in the list and append it to the end? Can you write this in a single line of code?
x = x[1:] + [x[0]]
print(x)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (2 minutes)
Would you use a for loop or a while loop?

1. Creating a letter counter based on a string
2. Trying to identify whether a dice is fair or not
3. Iterating over a list to identify multiples of 5
4. Creating a selection for an individual based on a given menu
5. Determine how long it might take to reach a certain threshold


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
Would you use a for loop or a while loop?

1. Creating a letter counter based on a string
    * `for` loop
2. Trying to identify whether a dice is fair or not
    * Potentially a while loop, where eventually you wish to converge at the expected value, at which point you might use break to exit. However, you could use a for loop with many many iterations, with an exit condition.
3. Iterating over a list to identify multiples of 5
    * `for` loop
4. Creating a selection for an individual based on a given menu
    * Potentially a `while` loop, though a `for` loop with a high count could be used as instead.
5. Determine how long it might take to reach a certain threshold
    * Potentially a `while` loop, with an exit condition for when the threshold is reached. However, a `for` loop could be used instead, where the `for` loop is allowed many many iterations, with an exit condition implied by the upper bound of the iteration count.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (8 minutes)
Write a for loop to print a menu out of this list with their number options starting at 1? Store the choices (as the item names, not the numbers) in a list. Print out the list containing the food ordered.

```python
food_lst = [‘Pancakes’, ‘Omelet’, ‘Toast’, ‘Waffles’, ‘Bacon’, ‘Sausage’, ‘Orange Juice’]
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python

```