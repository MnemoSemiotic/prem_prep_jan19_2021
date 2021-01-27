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
