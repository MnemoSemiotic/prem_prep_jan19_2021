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
