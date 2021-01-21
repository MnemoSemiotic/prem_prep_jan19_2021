# Basics of Python Functions
* Function Parameters
* Printing vs Return
* Global vs Local Scope


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# More Quick Notes on Slack Etiquette
* Comment on the appropriate thread/channel, if possible, rather than sending a message out to the whole group
* Use three backticks to create a code block

```
# put your code within triple ticks to render them
#   as text editor text
```

* Use a single backtick on either side of some text to create an inline block, helpful for function names, operations, etc:
    * `some_function()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (2 minutes)
* What are the 4 scalar types we briefly discussed?
* What does `print(1/100**100000)` give us and why?
* What does `3 == 3` evaluate to?
* What does `2 != 2` evaluate to?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
* What are the 4 scalar types we briefly discussed?
    * `int, float, bool, str`
* What does `print(1/100**100000)` give us and why?
    * `0`, because the value is too small to represent with a `float`
* What does `3 == 3`  evaluate to? 
    * `True`
* What does `2 != 2` evaluate to?
    * `False`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
* What response will this code produce when:
    * `x = 9` 
    * `x = 80` 
    * `x = 25` 
    * `x = 66`

```python
if x % 5 == 0:
    print(‘High Five!’)
elif x % 2 == 0 and x % 5 == 0:
    print(‘Gimme 10!’)
elif x % 2 == 0:
    print(‘Evens!’)
else:
    print(“I got nothing”)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

* What response will this code produce when:
    * `x = 9` 
        * `I got nothing`
    * `x = 80` 
        * `High Five!`
    * `x = 25` 
        * `High Five!`
    * `x = 66`
        * `Evens!`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
