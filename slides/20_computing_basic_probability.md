# Computing Basic Probabilities
* Cardinality


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Cardinality
* Can be thought of as the "magnitude" or number of elements that compose a subspace
* Representation of cardinality of a sample space $S$ and some event $A$
    * $S$ = {1, 2, 3, 4, 5, 6, 7, 8}
        * $|S|$ = 8
    * $A$ = {1, 2, 3, 4}
        * $|A|$ = 4



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Probability as ratio of Cardinality
* $S$ = {1, 2, 3, 4, 5, 6, 7, 8}
    * $|S|$ = 8
* $A$ = {1, 2, 3, 4}
    * $|A|$ = 4
* $A$ is clearly a subset of $S$

$$
P(A) = \frac{|A|}{|S|}
$$

$$
P(A) = \frac{4}{8}
$$

$$
P(A) = 0.5
$$

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Simple Probability Example

What is the probability of rolling a fair six-sided die, and the result of the roll shows an even number of pips?

Step 1 - Determine the Cardinality of the sample space and of the event
* $S$ = { ⚀, ⚁, ⚂, ⚃, ⚄, ⚅ } ; $|S|$ = 6
* $A$ = Even number of pips showing = { ⚁, ⚃, ⚅ }; $|A|$ = 3

Step 2 - Calculate the probability
* $P(A) = \frac{|A|}{|S|} = \frac{3}{6} = \frac{1}{2} = .5$


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Probability Notation

| Notation | Meaning |
|----------|---------|
|$P(A)$    | Probability of A|
|$P(\text{not}  A)$    | Probability of A Complement|
|$P(AB)$    | Probability of A intersect B|
|$P(A \cup B)$    | Probability of A union B|
| $ P(A \mid B) $    | Probability of A given B|


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Building a Sample Space through counting
* Can consider elements of a set as "numbers" in a counting system, where the cardinality is the "base" of that system.

Example: Counting using pets

$S$ = {cat, dog, ferret, goldfish}

List all the possible outcomes for 4 pets, randomly selected *with replacement*

```python
pets = ['cat', 'dog', 'ferret', 'goldfish']

pet_outcomes = []

for pet1 in pets:
    for pet2 in pets:
        for pet3 in pets:
            for pet4 in pets:
                pet_outcomes.append([pet1, pet2, pet3, pet4])

for pet_outcome in pet_outcomes:
    print(pet_outcome)

# ['cat', 'cat', 'cat', 'cat']
# ['cat', 'cat', 'cat', 'dog']
# ['cat', 'cat', 'cat', 'ferret']
# ['cat', 'cat', 'cat', 'goldfish']
# ['cat', 'cat', 'dog', 'cat']
# ['cat', 'cat', 'dog', 'dog']
# ['cat', 'cat', 'dog', 'ferret']
# ...
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Breakout (4 minutes)
* Reference the previous slide

What is the probability that a person will select 2 or more cats when randomuly choosing 4 pets (with replacement)?

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Breakout SOLUTION
* Reference the previous slide

What is the probability that a person will select 2 or more cats when randomly choosing 4 pets (with replacement)?

```python
# ... utilize previous code to build sample space

two_plus_cats = []

for pet_outcome in pet_outcomes:
    if pet_outcome.count('cat') >= 2:
        two_plus_cats.append(pet_outcome)

print(len(two_plus_cats) / len(pet_outcomes)) # --> 0.2617

```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Breakout (4 minutes)
Write a function called `series_of_flips`.
* define one parameter, `n`, which represents the number of coin flips
* return a list of length `n` containing `n` random coin flips


```python
from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Breakout Solution
Write a function called `series_of_flips`.
* define one parameter, `n`, which represents the number of coin flips
* return a list of length `n` containing `n` random coin flips


```python
from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips
```
