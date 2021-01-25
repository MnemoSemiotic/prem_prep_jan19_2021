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
