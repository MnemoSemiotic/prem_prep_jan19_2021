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