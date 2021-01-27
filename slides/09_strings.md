# Strings
* Declaring `strings`
* `string` methods
* Functions with `strings`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `string` datatype
* Strings are simply a collection of characters
* However, in Python, a `string` is a scalar type and is immutable
* Strings are declared with single, double, or triple quotes. 
    * Mostly interchangeable. Single and double quotes only work with strings that span one line. 
    * Strings that span multiple lines need to be declared using triple quotes.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Basic `string` Operators 
* We can use the addition operator to concatenate strings.
    * `'My first string ' + 'My second string'` => `'My first stringMy second string'`
* The multiplication operator will repeat the string `n` times. 
    * `'Repeating string' * 3` => `'Repeating stringRepeating stringRepeating string'`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Casting to and from a `string`
* Just about any data type can be cast to a `string`.
    * Use the `string` casting function: `str()`
* Not every `string` can be cast to another data type.
    * `int('a')` will not work
* String concatenation will only work between strings
    * Need to cast any numeric variables to a `string` before concatenating. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Join a `list` to create a `string`
* Use the `join` `string` method to create a single `string` that contains all the elements of a `list`. 
    * `''.join(list)`
* All the elements of the `list` must be strings for the `join` method to work
    * You can use the `map` function to quickly cast all the elements of a `list` to strings 
    * `list(map(str, list))`



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `string` Slicing
* Use slice indexing (similar to a list) to access characters or subsequences of characters
* `string[index]`
* `string[start:end]`
* `string[start:end:skip]`

