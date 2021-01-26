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