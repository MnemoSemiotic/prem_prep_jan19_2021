# Python Variables and Logic
* Declaring Variables
    * Variable Naming Syntax
* Logic Operators
* Control Flow
* Homework

<br><br><br><br><br><br><br><br><br>


----------------------------------------------------------------
# Variables
* You can think of variable assignment as giving a name to something so that it can be accessed later by different parts of your program.
    * You can use a variable to store any data type
    * Important for **reusability**


<br><br><br><br><br><br><br><br><br>


----------------------------------------------------------------
# Declaring Variables  
* Variables are assigned using the `=` operator.
    * variable = value
* Need to print to see the result of assigning a variable.
* Can assign two or more variables on the same line.
    * `x, y = 1, 2`


<br><br><br><br><br><br><br><br><br>


----------------------------------------------------------------
# Give it a good name
* You should strive to give your variables well-defined, succinct names
* Variable naming conventions are covered in [PEP 8](https://www.python.org/dev/peps/pep-0008/).
* Use **snake case** to name variables:
    * Replace spaces with _
    * `this_is_a_variable = 8`
* There are some reserved words that can’t be used as variable names.
    * [Python reserved words list](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)


<br><br><br><br><br><br><br><br><br>


----------------------------------------------------------------
# Boolean Operators

| Operator              | Meaning                 |
| ----------------------| ----------------------- |
| <center>`>`</center>  | Greater Than            |
| <center>`>=`</center> | Greater Than or Equal   |
| <center>`<`</center>  | Less Than               |
| <center>`<=`</center> | Less Than or Equal      |
| <center>`==`</center> | Equals or Is Equivalent |
| <center>`!=`</center> | Does not Equal          |

```python
print(5 > 4)   # --> True
print(5 >= 6)  # --> False
print(5 < 4)   # --> False
print(5 <= 6)  # --> True
print(5 == 6)  # --> False
print(5 != 6)  #--> True
```


<br><br><br><br><br><br><br><br><br>


----------------------------------------------------------------
# Logical Operators
* Operator Precedence: `not`, `and`, `or`


```python
print(not True)       #--> False
print(not False)      #--> True
print(True and True)  #--> True
print(True and False) #--> False
print(True or False)  #--> True
```


<br><br><br><br><br><br><br><br><br>


----------------------------------------------------------------
# BREAKOUT (2 mins)
What is the result of the following boolean expression?

```python
(not (not (True or False) and (True and True))) and True or True
```


<br><br><br><br><br><br><br><br><br>


---------------------------------------------------------------
# BREAKOUT Solution

What is the result of the following boolean expression?
* note that the `or True` on the end will evaluate the whole thing as `True`. We'll simplify the whole thing anyway

```python
(not (not (True or False) and (True and True))) and True or True
#          --simplify---
(not (not True and (True and True))) and True or True
#     --------
(not (False and (True and True))) and True or True
#                -------------
(not (False and True)) and True or True
#     --------------
(not False and True or True
#---------
True and True or True
#------------
True or True
#----------
True
```


<br><br><br><br><br><br><br><br><br>


---------------------------------------------------------------
# Bitwise Operators: `~`, `&`, `|`
* `~`, `&`, `|` are the matching bitwise operators for `not`, `and`, and `or`
* Don’t use these or worry about them for now
* They may not behave exactly as you expect


<br><br><br><br><br><br><br><br><br>


---------------------------------------------------------------
# Exclusive or (XOR)
* `^` is the bitwise operator for **exclusive or**
* For now, think of this as asking the question **“are these two things different?”**


<br><br><br><br><br><br><br><br><br>


---------------------------------------------------------------
# Order of Logical Operators


|  Order of Operations    |
|-------------------------|
| <center> ~ </center>    |
| <center> & </center>    |
| <center> ^ </center>    |
| <center> | </center>    |
| <center> not </center>  |
| <center> and </center>  |
| <center> or </center>   |


<br><br><br><br><br><br><br><br><br>


---------------------------------------------------------------
# BREAKOUT (3 minutes)
### What do each of these return?
* `not 7 > 2`
* `3 >= 2 or 5 < 1`
* `not 8 `
* `bool(‘’) and 5 != 3`
* `bool(‘’) and 5 != 5`


<br><br><br><br><br><br><br><br><br>


---------------------------------------------------------------
# BREAKOUT Solution
### What do each of these return?
* `not 7 > 2`
    * `False`
* `3 >= 2 or 5 < 1`
    * `True`
* `not 8 `
    * `False`
* `bool(‘’) and 5 != 3`
    * `False`
* `bool(‘’) and 5 != 5`
    * `False`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Control Flow: if/else

![if flow](images/if_flow.png)


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# if
* We use if statements if we want to evaluate code only under a certain condition
* Only when the statement following the if keyword evaluates to True will Python run the code in the body of the if block
* Syntax:

```python
if some_condition:
    # execute this code
else:
    # execute this code
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# if/elif/else
* Often, we will want to execute some other code if the condition in the if statement is not met.
    * Use an if-else statement
* What if we want to check multiple conditions?
    * Use if-elif-else
    * You can use multiple elif statements
    * Order matters!

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# if/elif/else syntax

```python
if some_condition:
    # execute this code
elif another_condition:
    # execute other code
elif yet_another_condition:
    # execute this code
else:
    execute some other code
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# if/elif/else
* We can incorporate comparison operators and logical operators into our if statements

```python
x = 7
y = False

if x < 10 and not y:
    print('all is well')
elif x > 3 and y:
    print('danger')
else:
    print('nothing matters')
```

will output

```python
# --> all is well
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)

* Write a code snippet that checks two numbers, `x` and `y`:
    * Check if the sum of two numbers is greater than both numbers
        * If it is, print `"Both numbers are positive"`
    * Check if the sum is equal to either number
        * If it is, print `"At least one number is zero"`
    * Otherwise, print `"At least one number is negative"`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT solution

```python
if x + y == x or x + y == y:
    print('At least one number is zero')
elif x + y > x and x + y > y:
    print('Both numbers are positive')
else:
    print('At least one number is negative')
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Homework

* Complete the Day 1 Homework if not completed
* Complete all Challenges in these Learn Sections
    * [Variables](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introPython/03_Variables/00_unit_overview.md)
	* [Scalar Types](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introPython/04_Scalar_Types/00_unit_overview.md)
	* [Basic Operators](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introPython/05_Basic_Operators/00_unit_overview.md)
	* [Control Flow](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introPython/06_Control_Flow/00_unit_overview.md)
