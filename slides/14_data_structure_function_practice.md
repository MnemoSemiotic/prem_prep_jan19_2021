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


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (15 minutes)
Create a text content analyzer. This is a tool used by writers to find statistics such as word and sentence count on essays or articles they are writing.

Write a Python program that analyzes string and compiles statistics on it. Your sentence can end in a `.`, `!` or `?`, do not include punctuation in your words

The program should PRINT using string formatting:
1. The total word count
2. The count of unique words
3. The number of sentences 
4. The average sentence length in words (whole number)
5. A list of words used, in order of descending frequency

The program should also `return` all the information in a dictionary
To get your string to check is on the next slide

Use this text:

```python
Mochi is a Maltese. He weighs only 4 lbs even though he is already 6 years old!!! He likes to eat blueberries. Mochi is sleeping. Is Mochi cute? Everyone thinks Mochi is cute!! Couple more lines for testing stdin. Is Disney Tsum Tsum a fun game?! Disney Tsum Tsum is very fun! Mochi is sleeping. Mochi loves Disney Tsum Tsum. Mochi is sleeping again.
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def word_counter(text_list):
    d = dict()
    out = []

    for word in text_list:
        if word not in d:
            d[word] = 0
        d[word] += 1
    
    for word, count in d.items():
        out.append((count, word))

    return [word for count, word in sorted(out, reverse=True)]

def text_content_analyzer(text):
    d = {
        'total_word_count': 0,
        'unique_word_count': 0,
        'sentence_count': 0,
        'avg_sentence_len': 0,
        'word_list_desc_freq': []
    }

    text_list = text.replace('.', '').replace('?', '').replace('!', '').lower().split(' ')
    sentences = text.replace('?', '.').replace('!', '.').lower().split('. ')
    sentences = [sentence.replace('.', ' ') for sentence in sentences]

    d['total_word_count'] = len(text_list)
    print(f'Total Word Count: {d['total_word_count']}')

    d['unique_word_count'] = len(list(set(text_list)))
    print(f'Unique Word Count: {d['unique_word_count']}')

    d['sentence_count'] = len(sentences)
    print(f'Sentence Count: {d['sentence_count']}')

    d['avg_sentence_len'] = sum([len(sentences) for sentence in sentences]) / len(sentences)
    print(f'Average Sentence Length: {d['avg_sentence_len']}')

    d['word_list_desc_freq'] = word_counter(text_list)
    print(f'Average Sentence Length: {d['avg_sentence_len']}')
```
