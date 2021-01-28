https://docs.google.com/presentation/d/1dZWsoak_vsQm0jWhU6rncxSvBohh4MITZ_K5gKpW5O0/edit#slide=id.p


# Data Structures Review
* Sets
* Tuples
* Dictionaries
* List, Dict, if/else comprehension






<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Review: Sets
* Sets are unordered, mutable collections
* Sets will only contain unique elements
* Sets can be declared:
    * Using the set constructor `set()`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)

```python
str1 = set('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.'.lower().replace('.', '').split(' '))
str2 = set('Complex is better than complicated. Flat is better than nested. Sparse is better than dense.'.lower().replace('.', '').split(' '))
```

* What is the intersection of str1 and str2?

* What is the union of str1 and str2?
* What is the difference of str1 - str2?
