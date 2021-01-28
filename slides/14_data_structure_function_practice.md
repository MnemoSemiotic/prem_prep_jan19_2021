# Function practice on data structures



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

# BREAKOUT (5 minutes)
Let’s warm up with something easy:

Write a function that will calculate the total amount of a dinner bill, given the total before tax, the tax rate, and percentage. Your function will accept these three values as arguments. It will then do the following:
* Apply the tax rate to the bill total
* Apply the tip percentage to the total amount
* Return the total amount of bill before and after tip.

Here’s an example of how you would call the function:

```python
bill_with_tax, bill_with_tax_and_tip = calc_total_bill(100, 0.10, 0.10)
bill_with_tax_and_tip

>>> 121.0
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def calc_total_bill(bill, tax, tip):
    bill_and_tax = bill * (1+tax)
    tax_and_tip = bill * (1+tax) * (1+tip)
    return bill_and_tax, tax_and_tip
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (7 minutes)
1. Write a list comprehension of this list to get the len of each item, if an item doesn't have a len, make sure to change that item to a string before you take len.
    * `L1 = ['hello', 'goodbye', [1,2,3], 44]`

2. Write a list comprehension that takes in a list of positive integers and adds 100 to a single digit number else it will subtract 100 from the number.
    * `L2  = [1, 5, 8, 100, 43, 254, 1000, 3, 0, 88888]`

3. Write a dictionary comprehension of a dictionary, making the values the keys and the keys the values
    * `D1 = {'Apple':5, 'Pear': 10, 'Banana':2, 'Orange': 1}`

4. Write a dictionary comprehension of a dictionary, adding '_test' to the keys and finding the remainder of the value when divided by 13
    * `D2 = {'a': 540, 'b': 222, 'c':88, 'd':1000,'e':13}`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
1.

```python
L1 = ['hello', 'goodbye', [1,2,3], 44]
l1 = [len(item) if not isinstance(item, (int, float, complex, bool)) else len(str(item)) for item in L1]
```

2.

```python
L2  = [1, 5, 8, 100, 43, 254, 1000, 3, 0, 88888]
l2 = [n + 100 if abs(n / 10) < 1 else n - 100 for n in L2>]
```

3.

```python
D1 = {'Apple':5, 'Pear': 10, 'Banana':2, 'Orange': 1}
d1 = {v: k for k, v in D1.items()}
```

4.

```python
D2 = {'a': 540, 'b': 222, 'c':88, 'd':1000,'e':13}
d2 = {k+'_test': v%13 for k, v in D2.items()}
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (8 minutes)
Create a function that will check to see if a book is in a library and if it isn’t, then update your library with the book and let the user know it was a new book, else tell the user that the book was not new.  (Remember capitalization matters) Return your library as a list
    a. Try this if your library was a list - use list methods 
    b. Try this if your library was a set - use set methods

```python
def book_update(new_book, library):
	pass
```

```python
library = [‘Catch-22’, ‘The Great Gatsby’, ‘Grapes of Wrath’, ‘Brave New World’, ‘To Kill a Mockingbird’, ‘Lord of the Rings’, ‘1984’, ‘Lord of the Flies’, ‘Moby Dick’]
```

Check to see if your library has these books:

```python
‘The Odyssey’, ‘catch-22’, ‘moby dick’, ‘The hitchhiker’s guide to the galaxy’
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def book_update(new_book, library):
    if new_book.lower() in [book.lower() for book in library]:
        print(f'Your book, {new_book}, is in the library')
        return library
    else:
        print(f'Your book, {new_book}, is new!')
        if isinstance(library, list):
            new_lib = library[:]
            new_lib.append(new_book)
            return new_lib
        elif isinstance(library, set):
            new_lib = library.copy()
            new_lib.add(new_book)
            return list(new_lib)
```