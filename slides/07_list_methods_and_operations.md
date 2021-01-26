# List Methods and Operations
* appending
* extending
* removing
* pop
* len
* sum
* sort
* reverse
* sorted
* reversed
* max
* min
* count
* any
* all
* enumerate
* parallel lists
* unpacking


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Appending to a `list`
* The `append` method places a new value at the end of the `list`. 
    * Syntax: `list.append(new_item)`	
* Can `append` a `list` to another `list` in order to create a nested `list`.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Extending a `list`
* The `extend` method combines two lists
    * Syntax: `list1.extend(list2)`	
    * In the above example, the `list2` elements will be inserted into `list1`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Removing Items From a `list`
* Use the `remove` method to remove an element from a `list`
    * Syntax: `list1.remove(some_item)`	
    * Only removes the first instance of that element
* Use `del` to remove a specific index of element, or slice of elements, in a `list`:
    * `del list[index]`
    * `del list[start:stop]`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# The `pop` method
* The `pop` method removes the last item from a `list` in place and returns the value of that last item
    * Syntax: `list_name.pop()`
* The value of the last item can be stored by assigning the method call to a variable
    * `last_element = list_name.pop()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# len and sum
* `len()` return the length of the `list` passed in
    * Syntax: `len(list_name)`
* `sum()` will calculate the sum of all the elements of the list that is passed in.
    * Syntax: `sum(list_name)`
    * Only works with lists that contain only integers and floats


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `sort`, `reverse`, `sorted`, and `reversed`
* The `sort` and `reverse` methods are slightly different from the `sorted` and `reversed` functions
* The `sort` method will sort all the values in a `list` in ascending order and change the `list` in place. `sorted` will return a `list` with elements sorted but does not modify the original `list`.
    * Syntaxes: 
        * `lst.sort()`
        * `sorted(lst)`
* The `reverse` method will reverse the list in place. `reversed` will return an iterable object that must be cast to `list` to be indexed and used as a `list`. In fact, list slicing is preferable to `reversed` when wanting to get a reversed list.
    * Syntaxes:
        * `lst.reverse()`
        * `reversed(lst) # returns an iterable object`
        * `lst[::-1]`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `max` and `min`
* `max()` returns the highest numeric value in a `list`
    * Syntax: `max(list_name)`
* `min()` returns the lowest numeric value in a `list`
    * Syntax: `min(list_name)`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `count`
* The `count` method will return a count the occurences of an item in a `list`.
* Syntax: `list.count()`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `any` and `all`
* A value where `bool(value) == True` can be considered ‘truthy’
* `any()` returns `True` if any of the values in a `list` are ‘truthy’
    * Syntax: a`ny(list_name)`
* `all()` returns `True` if all of the values in a `list` are ‘truthy’
    * Syntax: `all(list_name)`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
* What would be the result of `len([1, 2, [1, 2]])`
* What would be the result of `list(reversed([1, 5, 6, 4, 2]))`
* What do the `max` and `min` functions do?
* What is the result of `any([0, 2, 5, 6])`? What is the result of `all(['', 'a', 'c', 'p'])`
* What will be stored in the variables `lst` and `last_element` after executing the following code?
    * `lst = [1, 3, 5, 7]`
    * `last_element = lst.pop()`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
* What would be the result of `len([1, 2, [1, 2]])`
    * Solution: `3`
* What would be the result of `list(reversed([1, 5, 6, 4, 2]))`
    * Solution: `[2, 4, 6, 5, 1]`
* What do the `max` and `min` functions do?
    * Solution: `max` returns the highest-valued element, `min` returns the lowest-valued element
* What is the result of `any([0, 2, 5, 6])`? What is the result of `all(['', 'a', 'c', 'p'])`
    * Solution: `True`, `False`
* What will be stored in the variables `lst` and `last_element` after executing the following code?
    * `lst = [1, 3, 5, 7]`
    * `last_element = lst.pop()`
    * Solution: lst: `[1, 3, 5]`, last_element: `7`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# `enumerate()`
* Sometimes you will need to write a `for` loop that can keep track of items in a `list` and their corresponding indices.
* Syntax: 

```python
for idx, num in enumerate(my_lst):
    some code
```

* `enumerate` needs two variables: the index gets assigned to the first variable and the item from the `list` gets assigned to the second

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Parallel Lists
* Two lists that have equal length and contain associated values at each index are parallel.
* The same index can be used in each of the parallel lists to access the related data. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Unpacking a nested `list`
* In the case of nested lists, we can use an accumulator to unpack the nested items into a new `list`. 
* In the new `list`, the nesting will be “undone.”


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Unpacking a nested `list`
* In the case of nested lists, we can use an accumulator to unpack the nested items into a new `list`. 
* In the new `list`, the nesting will be “undone.”

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
* Create a function that will iterate over a `list` printing out each value of the `list` squared and the indexed position of each item starting at an index of `1` instead of `0`.

```python
sample_data = [2, 4, 6, 8, 10, 12, 14]
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def squared_with_indices(num_list):
    for idx, num in enumerate(num_list, 1):
        print(num**2, idx)

squared_with_indices(range(1, 20))
```