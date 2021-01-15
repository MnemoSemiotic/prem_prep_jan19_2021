----------------------------------------------------------------
# Introduction to Python
* What is Python?
* Interpreted vs. Compiled Languages
* Python Resources
* Text Editors
* How to Program 
* Comments
* Extra (depending on time)
    * Simple Operators in Python

----------------------------------------------------------------
# What is Python?
* Python is a general-purpose programming language that can be used to:
    * develop web apps and software
    * write scripts to automate operations within operating systems
    * operate robots and other technical machinery
    * … and more!

----------------------------------------------------------------
# Python for Data Science
* Python is one of many languages in Data Science and Machine Learning. It is by far the most popular.
* Python is easy to learn, read and write.
* There are extensive scientific computing libraries and published academic work that uses Python

----------------------------------------------------------------
# Start off using repl.it to run your code
* Create an account and open up a new Repl now!
![Sign up for repl](images/sign_up_for_repl.png)

----------------------------------------------------------------
# Python is an Interpreted Language
* Interpreted languages are translated into machine code and run at the same time, giving immediate output.
* In repl.it, you can just hit the “Play” button and see results
![repl, interpreted lang](images/interpreted_language.png)
* Interpreted languages: Javascript, Ruby, LISP, many other

----------------------------------------------------------------
# Compiled Languages
* A compiled language requires that your code be translated into a more fundamental machine language before it is run. This leads to a workflow of:
    * Write/Edit Code
    * Compile Code
    * Run the compiled executable
* Compiled languages: C/C++, Java/Scala (sort of), Rust

----------------------------------------------------------------
# Python Documentation and Resources 
* [Python Documentation ](https://docs.python.org/3/)
* [Pep 8 Style Guide ](https://www.python.org/dev/peps/pep-0008/)
* Try using Google first, before asking peers or instructors , for example:
![Google First](images/google_things.png)
* Practice on [CodeWars.com](http://codewars.com)

----------------------------------------------------------------
# Text Editors 
* Text editors are used to write plain text (using [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding)
* DSI and Galvanize courses use [VSCode](https://code.visualstudio.com/) primarily, please install it ASAP
* Install [Anaconda](https://www.anaconda.com/distribution/) for your operating system, giving you access to Jupyter notebooks


----------------------------------------------------------------
# How to Program 
* Think about the problem 
* Define what it means for the program to be working 
* Create a series of formal steps that lead to a repeatable operation

----------------------------------------------------------------
# Think about the problem 
* Broadly define what you are trying to do. 
* Does your problem have a specific outcome that you want to obtain?

----------------------------------------------------------------
# Define what it means for the program to be working 
* Prior to writing any code, understand what a solution or what success is in your program
    * Is it suppose to print something?
    * Are you creating a new variable?
    * Are you changing an existing variable?

----------------------------------------------------------------
# Create a series of steps for a repeatable operation
* Think about how to obtain your solution in small definable steps.
* If necessary, write “Pseudocode” that describes the general algorithm for what you are trying to accomplish
* Write code (as in, translate Pseudocode into Python)

----------------------------------------------------------------
# BREAKOUT (5 minutes)
### Write an algorithm for boiling a box of spaghetti
* Define the steps clearly and at an appropriate level for an extra-terrestrial with good human language skills, who has never cooked pasta before
* There is no single correct solution here

----------------------------------------------------------------
# BREAKOUT SOLUTION EXAMPLE (abbreviated)
1. Gather cooking implements and supplies
    a. Take Boiling Pot out of cupboard under the counter
    b. Take Box of Spaghetti out of cupboard next to refrigerator
    c. Take Salt from spice rack
    d. Take oil from shelf next to stove
2. Prepare water for boiling pasta
    a. Fill Boiling Pot with water from the tap
    b. Place Boiling Pot on stove burner
    c. Turn heat dial clockwise so that it is on high
    ...

----------------------------------------------------------------
# Comments

```python
# this is a single line comment
```

```python
'''
This
is a 
multi-line
comment
'''
```

----------------------------------------------------------------
# Reasons for using comments
* Send a message to someone reading your code	
* Exclude some code snippet from running 
* Provide function documentation 
* Leave TODO: statements in your code, for later development

----------------------------------------------------------------
# Basic Python Constructs
* Common Data Types 
* Simple Operators in Python
* Assignment Operators

----------------------------------------------------------------
# Common Data Types 

* A **data type** can be thought of as _a form in which a piece of data can exist_
    * Working with integers, floats, booleans


* the `type()` function will tell you the data type 
    * ex: `type(23)` will tell you that 23 is an integer


----------------------------------------------------------------
# Number Types: `int`, `float`, and `bool`
* Integers can be thought of as “whole numbers”
* Floats can be thought of as “decimal numbers”
* Ints and floats are encoded differently
    * `1.0 == 1` ?? ⇒ `True`
    * However, `type(1.0) == type(1)` ?? ⇒ `False`

----------------------------------------------------------------
# BREAKOUT (3 minutes):
* Use the `type()` function to discover the type of the number `74`.
* Describe simply what you did on the line above your code snippet

----------------------------------------------------------------
# BREAKOUT SOLUTION:

```python
# output to console the type of 74
print(type(74))
```

NOTE: In general, you will want to avoid writing comments that say what your code is doing, unless, at this stage, it is for your own benefit and study

----------------------------------------------------------------
# Simplest Operators in Python
* Basic Arithmetic Operators: 
    Addition: `+`
    Subtraction:  `-` 
    Multiplication:  `*`
    Division: `/`
* PEMDAS
    * Use parentheses `(3+5) / 7` to ensure the desired order of operations


----------------------------------------------------------------
# Duck Typing
* Python is a “duck typed” language
    * _"If it walks like a duck, and quacks like a duck, then it must be a duck."_
    * Effectively, this means that you can perform mathematical operations between similar types, such as ints and floats, because Python infers a general type for the operation.
        * For example, operations between ints and floats will result in float results
        * Division will result in a float


----------------------------------------------------------------
# BREAKOUT (5 minutes)
* Add 5 and 7.2, multiply the result by 6, divide that result by 3, then square the result

----------------------------------------------------------------
# BREAKOUT SOLUTION
* Add 5 and 7.2, multiply the result by 6, divide that result by 3, then square the result

```python
print((((5 + 7.2) * 6) / 3)**2)
```

----------------------------------------------------------------
# Homework
* Read through the [Welcome to Data Science](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-init/00_purpose/00_ds_prep_welcome_overview.md) Prep Section
* Read the first 3 units in [Introduction to Python](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introPython/00_Welcome_to_Python/00_course_overview.md)
    * [Welcome to Python](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introPython/00_Welcome_to_Python/00_course_overview.md)
    * [About Python Programming](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introPython/01_About_Python_Programming/00_unit_overview.md)
    * Complete all the challenges in [Python Basics](https://learn-2.galvanize.com/content_link/github/gSchool/dsi-prep-module-introPython/02_Python_Basics/00_unit_overview.md)
* Install [VSCode](https://code.visualstudio.com/)
* Set up a GitHub account [http://github.com](http://github.com)
    * Share your github username
    * Follow [clownfragment](https://github.com/clownfragment/) and [clarkwalker](https://github.com/clarkwalker/)
* Set up a CodeWars account at [http://codewars.com](http://www.codewars.com/r/xCbgXQ) 
