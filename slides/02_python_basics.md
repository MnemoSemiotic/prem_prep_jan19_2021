# Python Basics
* Common Data Types 
* Simple Operators in Python
* Assignment Operators
* Scalar Data Types 
* Declaring Variables
    * Variable Naming Syntax
* Logic Operators	
* Control Flow
* Homework










<br><br><br><br><br><br><br><br>

----------------------------------------------------------------
# Numeric Data Types 
* A data type can be thought of as a form in which a piece of data can exist
    * `int`   :  whole numbers
    * `float` :  decimal numbers
    * `bool`  :  `True` or `False`
* The `type()` function will tell you the data type:

```python
print(type(34)) # --> <class 'int'>
print(type(72.935)) # --> <class 'float'>
print(type(True)) # --> <class 'bool'>
```

----------------------------------------------------------------
# Numeric Type Encoding
* `int` and `float` datatypes are encoded differently, but are able to share operators in Python. 
    * Notice the values are considered equivalent, while the type of each data is different:

```python
print(1.0 == 1) # --> True
print(type(1.0) == type(1)) # --> False
```

----------------------------------------------------------------
# Python is a “duck-typed” language
* _"If it walks like a duck, and quacks like a duck, then it must be a duck."_
* The data type is automatically inferred
* Gives ability to share operations between data type through type inference:

```python
print(type(1)) # --> <class 'int'>
print(type(1.3)) # --> <class 'float'>
print(type(1 == 1.0)) # --> True
print(type(1 == 1.9)) # --> False> 
```

----------------------------------------------------------------
# Simple Operators in Python
* Basic Arithmetic Operators: `+`, `-`, `*`, `/`
* Floor Division: `//`
* Modulo: `%`
* Order of Operations: PEMDAS
* Exponentiate: `**`
* Casting: `int(x)`, `float(x)`

----------------------------------------------------------------
# Basic Arithmetic Operators
The basic arithmetic operators are intuitive and follow basic PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)

```python
print(2**2)             # --> 4
print(2 * 2)            # --> 4
print(2 / 2)            # --> 1.0
print(2 + 2)            # --> 4
print(2 - 2)            # --> 0
print((2 + 2)**(3 - 2)) # --> 4
```

----------------------------------------------------------------
# BREAKOUT (2 minutes)
* print the result of multiplying by 7 the addition of 6 and 3
* print the product of 7 times 6, squared, with 23 subtracted from the result
* print the division of the result of 4 minus 2 times 2 into twenty

----------------------------------------------------------------
# BREAKOUT Solution:
* print the result of multiplying by 7 the addition of 6 and 3

```python
print(7 * (6 + 3)) # --> 63
```

* print the product of 7 times 6, squared, with 23 subtracted from the result

```python
print((7 * 6)**2 - 23)) # --> 1741
```

* print the division of the result of 4 minus 2 times 2 into twenty

```python
print((20 / (4 - 2 * 2)) # --> Will throw an error in this interpretation
# or
print((4 - 2) * (20 / 2)) # --> 20
```

----------------------------------------------------------------
# Floor Division
`//`
* Truncates anything after the decimal,
    * gives an int if both data types are int
* `x // y`: Returns the quotient of x divided by y

```python
print(20 // 4)     # --> 5
print(100 // 102)  # --> 0
print(27 // 3)     # --> 9
print(72.6 // 3.3) # --> 21.0
print(72 // 3.3)   # --> 21.0
print(72.6 // 3)   # --> 24.0
```

----------------------------------------------------------------
# Modulo
`%`
* Returns the remainder after dividing y into x
* Wildly helpful, as it turns out
    * can check even-ness or odd-ness using `num % 2`
    * can check divisibility

```python
if num % 2 == 0: print('num is even')
if num % 2 == 1: print('num is odd')
if num % 4 == 0: print('num is divisible by 4')

print(21 % 4) # --> 1
print(20 % 4) # --> 0
print(5 % 20) # --> 5
print(6 % 20) # --> 6
```

----------------------------------------------------------------
# Modulo with `float` values
* _Hand-wavey_: Avoid this unless you are clear on what you are doing
* Precision of the modulo operation is relative to the depth of the float
* Note the precision error!

```python
print(72.6 % 3.3)   # -> 3.299999999999998
print(72.6 % 3.33)  # -> 2.669999999999993
print(72 % 3.3)     # -> 2.7000000000000037
print(72.6 % 3)     # -> 0.5999999999999943

```

----------------------------------------------------------------
# Negative Modulo
* Negative modulo can be easily confusing. Avoid it unless it is key and you have a solid understanding of why you’re using it.

```python
print(21 % -5)  # -> -4
print(-21 % 5)  # ->  4
print(5 % -2)   # -> -1
print(-5 % 2)   # ->  1
```

----------------------------------------------------------------
# BREAKOUT (3 minutes)
1. If 3 letter carriers must deliver the same exact number of letters, and there are 299 letters, how many letters will not be delivered? Write a Python expression that answers this question.

2. If you have 5 bank tellers and 28 people waiting to be served, what is the least number of people who will not be served if it takes exactly 4 minutes to serve each person and the bank MUST close in 20 minutes? Write a Python expression that answers this question.

----------------------------------------------------------------
# BREAKOUT SOLUTION Part 1
1. If 3 letter carriers must deliver the same exact number of letters, and there are 299 letters, how many letters will not be delivered? Write a Python expression that answers this question.

```python
print(299 % 3) # --> 2
```

----------------------------------------------------------------
# BREAKOUT SOLUTION Part 2
2. If you have 5 bank tellers and 28 people waiting to be served, what is the least number of people who will not be served if it takes exactly 4 minutes to serve each person and the bank MUST close in 20 minutes? Write a Python expression that answers this question.

```python
print(28 - (20//4 * 5)) # --> 3
```

----------------------------------------------------------------
# REVIEW BREAKOUT  
* What are the two types of comments?
* What does the `type()` function do?
* What are some differences between the `int` and `float` types?

----------------------------------------------------------------
# REVIEW BREAKOUT Solution
* What are the two types of comments?
    * Single-line comments: `# this is a single line comment`
    * Multi-line comments:

```python
'''
This is a 
multi-line
comment
'''
```

* What does the `type()` function do?
    * Returns the data type of an object
* What are some differences between the `int` and `float` types?
    * An `int` is a whole number, a `float` is a decimal number
    * They are encoded differently in memory


----------------------------------------------------------------
# Casting
* Casting: `int(x)` or `float(x)`
    * _Convert a value to a different data type

```python
print(4 / 3)       # --> 1.3333333333333333
print(int(4 / 3))  # --> 1
print(float(7))    # --> 7.0
print(float(0))    # --> 0.0
```

----------------------------------------------------------------
# Assignment Operator 
* ex `x = 4`
* Variable Assignment: giving a name through which a value can be referred
* Operations on a variable will be determined by the data type of the value stored.
* Helps us keep track of values that change or values that are inputted 

----------------------------------------------------------------
# Incrementation Operators 
* Operations that modify the current value stored in a variable 
* `+=`, `-=`, `*=`, `/=`, etc. 
* Modifying the value referred to by a scalar type variable value will change the location in memory. Test this using the `id()` function

```python
x = 4
print(id(x))

x -= 2
print(id(x))
```

----------------------------------------------------------------
# What is a scalar type? 
* A scalar type holds one single value
* So far, we’ve mostly dealt with scalar types: `int`, `float`, `bool`
* Other scalar types are `string`, `None`, `complex`, `byte`

----------------------------------------------------------------
# Integers
* Integers are whole number values
* Can cast scalar data types to an integer using `int()`
* Using `int()` on a `float` always rounds down to the nearest integer

----------------------------------------------------------------
# Floats
* a `float` can be thought of as **continuous** while an `int` can be thought of as **discrete**
* Sometimes, we will consider two `float` values to be essentially equal if the difference is below some threshold.
* **Underflow** occurs when trying to represent a number that is smaller than the computer can represent in binary.
    * Can lead to unexpected behavior

----------------------------------------------------------------
# Booleans
* `True` or `False`
* Can be `1` or `0` when cast to a numeric type
* Non-zero and non-empty values return as `True`
* `not` negates a boolean
* Result of comparison operators is a `bool`

----------------------------------------------------------------
# Strings
* A `string` is an object that acts as a sequence of characters
* Declare a `string` using quotes 
* Can **concatenate** a `string` with another `string` using the `+` operator
* Note we will talk more about the `string` type in a later lecture

----------------------------------------------------------------
# `None` Type 
* `None` is not the same as `0`.
* Rather, `None` is the absence of a value
* **Functions without an explicit `return` will `return` `None`**

----------------------------------------------------------------
# BREAKOUT (2 minutes)
* What is the result of calculating `1/10**1000000`? Explain this result
* What is the result of `bool(‘’)`?
* What is the result of `bool(‘’ + ‘Hi’)`?

----------------------------------------------------------------
# BREAKOUT Solution
* What is the result of calculating `1/10**1000000`? Explain this result
    * `0.0`
* What is the result of `bool(‘’)`?
    * `False`
* What is the result of `bool(‘’ + ‘Hi’)`?
    * `True`

----------------------------------------------------------------
# Variables 
* You can think of variable assignment as giving a name to something so that it can be accessed later by different parts of your program. 
    * You can use a variable to store any data type 
    * Important for **reusability**

----------------------------------------------------------------
# Declaring Variables  
* Variables are assigned using the `=` operator. 
    * variable = value
* Need to print to see the result of assigning a variable. 
* Can assign two or more variables on the same line. 
    * `x, y = 1, 2` 

----------------------------------------------------------------
# Give it a good name
* You should strive to give your variables well-defined, succinct names
* Variable naming conventions are covered in [PEP 8](https://www.python.org/dev/peps/pep-0008/).
* Use **snake case** to name variables:
    * Replace spaces with _ 
    * `this_is_a_variable = 8`
* There are some reserved words that can’t be used as variable names. 
    * [Python reserved words list](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) 

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

----------------------------------------------------------------
# BREAKOUT (2 mins)
What is the result of the following boolean expression?

```python
(not (not (True or False) and (True and True))) and True or True
```

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

---------------------------------------------------------------
# Bitwise Operators: `~`, `&`, `|`
* `~`, `&`, `|` are the matching bitwise operators for `not`, `and`, and `or`
* Don’t use these or worry about them for now
* They may not behave exactly as you expect



---------------------------------------------------------------
# Exclusive or (XOR)
* `^` is the bitwise operator for **exclusive or**
* For now, think of this as asking the question **“are these two things different?”**

---------------------------------------------------------------
# Order of Logical Operators 

|  Order of Operations  |
|-----------------------|
| <center> ~ </center>  |
| <center>  </center>  |
| <center> ~ </center>  |
| <center> ~ </center>  |
| <center> ~ </center>  |
| <center> ~ </center>  |
| <center> ~ </center>  |