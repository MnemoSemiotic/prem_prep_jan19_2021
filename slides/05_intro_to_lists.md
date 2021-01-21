# Lists
* What is a `list` 
* Range
* List indexing
* List Membership
* List Slicing
* Nested Lists
* List Mutability
* Copy a List
* Append to a List
* Unpacking a list


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Describing a `list`
* A list is a **collection** of arbitrary objects
* Lists are **ordered** and **mutable**
* Declare empty lists using `[]` or `list()`

```python
lst_1 = []
lst_2 = list()
```

* Declare a list with values using [1, 2, 3]

```python
lst_3 = [1, 2, 3]
```

* Lists can hold both **scalar** types and collections

```python
nested_list = [[2, 3, 4], [2, 1, 5]]
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `range` Function
* The `range` function helps us create a `list` of contiguous integers.
* Syntax:
    * `range(start, stop, step)`
    * Start is inclusive, stop is not
* Returns an iterator object. Need to cast this object to a list so that we can work with it at this stage.

```python
one_to_99 = list(range(1,99+1))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `list` Indexing
* We use square brackets `[idx]` to access elements in a `list`
* Python uses **zero-based indexing**. Therefore, we count starting from 0.
    * `lst[0]` will return the first element of the list
* List indexing also allows us to reassign the value at that index
* Lists can be unpacked into variables.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `list` Membership
* Use the in keyword to check whether an element is in a list
    * `5 in [1, 2, 3, 4]` will be `False`
* You can conversely use not in to check if an element is not a member of the list
    * `5 not in [1, 2, 3, 4]` will be `True`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# List Slicing
* Use list slicing if you want to access a portion of a list
    * Notation is similar to indexing, e.g. `[1:3]`
    * Syntax: `list[start:stop]`
        * The slice starts at the start value and goes up until the stop value
        * The slice will not inclued the stop value
* Like the range function, we can specify a step
    * Syntax: `list[start:stop:step]`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Nested Lists
* A list that contains another list is known as a nested list
    * Example: `lst = [‘a’, ‘b’, [1, 2, 3]]`
* To access an element in a nested list, you will need two indices
    * `lst[2][0]` will access the value `1`  
* To access more than one element in a nested list, use a slice:	
    * `lst[2][:2]` will produce the slice `[1, 2]`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
`num_list = list(range(4, 16))`

* How do you index `num_list` to get `6`? How about `15`?
* How do you slice `num_list` to get this sublist: `[10, 11, 12, 13, 14, 15]`
* How do you slice `num_list` to get this sublist: `[4, 6, 8, 10, 12, 14]`
* Challenge: How do you slice `num_list` to get this sublist: `[8, 7, 6, 5, 4]`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
`num_list = list(range(4, 16))`

* How do you index `num_list` to get `6`? How about `15`?
    * `print(num_list[2]`
    * `print(num_list[11]`
* How do you slice `num_list` to get this sublist: `[10, 11, 12, 13, 14, 15]`
    * `print(num_list[6:13])`
* How do you slice `num_list` to get this sublist: `[4, 6, 8, 10, 12, 14]`
    * `print(num_list[6:13])`
* Challenge: How do you slice `num_list` to get this sublist: `[8, 7, 6, 5, 4]`
    * `print(num_list[4::-1])`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# List Mutability
* Lists are mutable
    * The contents in a `list` can change while its `id()` stays the same.
    * Two lists that contain the same values will have different ids. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Copy a `list`
* Create a copy of a list with the `.copy()` method
    * Syntax: `lst_2 = lst.copy()`
* `list` slicing can also be used to make a copy
    * Syntax: `lst2 = lst[:]`
* It is good practice to not modify function arguments. If a function argument is a `list`, create a copy before changing that `list` in any way. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `append()` to a `list`
* The `.append()` method places a new value at the end of the `list` 
    * Syntax: `lst.append(new_item)`	
* Can append a `list` to another `list` in order to create a nested `list`.

