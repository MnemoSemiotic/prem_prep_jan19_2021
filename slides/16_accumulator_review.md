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