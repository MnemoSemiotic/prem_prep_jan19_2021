# General Analytic Approach
* Counting
* Random Sampling
* Closed Formula


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# A Simple, General Analytic Approach
Considering a stochastic process, model or create a sample space and analyze:
1. Synthesize outcomes, model a phenomenon, look at data
2. Observe or interpret values
3. Answer questions



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Analysis through Counting
This can often be thought of as an "exhaustive" approach, for discrete outcomes, or a "bins" approach for continuous outcomes.

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Counting Example:
In a particular table top game, when in a battle, a player first rolls a 36-sided die, then pulls a card from a standard deck of cards. Finally, the player flips a coin three times.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 1. Synthesize Outcomes by counting

```python
rolls = range(1, 36+1)

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
card_nums = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Ace', 'Jack', 'Queen', 'King']

cards = []

for suit in suits:
    for card in card_nums:
        cards.append(f'{card} of {suit}')

# for card in cards:
#     print(card)

# print(len(cards))

coin_flips = []
for flip1 in ['T', 'H']:
    for flip2 in ['T', 'H']:
        for flip3 in ['T', 'H']:
            coin_flips.append([flip1, flip2, flip3])


S = []
for roll in rolls:
    for card in cards:
        for flip in coin_flips:
            S.append([roll, card, flip])

```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 2. Observe/Interpret values in a list

```python

for outcome in S:
    print(outcome)

print(len(S))
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
## 3. Answer Questions

Suppose that the 36-sided die represents the range of an attack. To hit an opponent, that opponent must be in range, for example, a roll of 29 will potentially hit another player 29 or less spaces away. The card represents the amount of damage that the attack will commit. In order to actually inflict damage, two of the three coin flips must be Heads.

**What is the probability of hitting an opponent that is 18 spaces away?**
* Write a code snippet that will provide the probability rounded to 3 places


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution

```python
hits = []
range_to_hit = 18

for outcome in S:
    if outcome[0] >= range_to_hit and outcome[2].count('H') == 2:
        hits.append(outcome)

print(f'proba: {round(len(hits) / len(S), 3)}')
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Random Sampling Example
* Can be used to approach a theoretical distribution and estimate parameters of that distribution

Consider invitations sent for a party (as if). 20 invitations are sent out. Each guest can possibly bring up to ten guests (with equal probability of between not going and 10 guests). No matter what, at least one person (you) will be at the party. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 1. Synthesize outcomes, model a phenomenon, look at data

```python
from random import choice

def num_attendees():
    num_peeps = 1

    for _ in range(20):
        num_peeps += choice(range(0, 11+1))

    return num_peeps
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 2. Observe or interpret values
* can pack into dictionary

```python

outcomes = dict()

for _ in range(100000):
    attending = num_attendees()

    if attending not in outcomes:
        outcomes[attending] = 0
    outcomes[attending] += 1

for k, v in sorted(outcomes.items()):
    print(f'{k}: {v}')
```

Notice that we are very unlikely to get less than 40 guests, and it is near impossible to get no guests in this scenario.

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT
## 3. Answer questions

Given a sample of outcomes, provide code to deliver an estimated probability that between 80 and 90 people will attend the party. Round the result to 3 decimal places.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution

```python
eighty_to_ninety = 0
total = sum(outcomes.values())

for attendees in range(80, 90+1):
    eighty_to_ninety += outcomes[attendees]

print(f'{round(eighty_to_ninety/total,3)}')
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Closed Formula Example

Consider a collection of spherical containers used to hold super gumballs of radius 1 inch. These containers range from 4 inch in radius up to 100 inches in radius. Consider a rough count of gumballs per sphere.

Spherical Volume:

$$
V = \frac{4}{3}\pi r^3
$$

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 1. Synthesize outcomes, model a phenomenon, look at data
$$
V = \frac{4}{3}\pi r^3
$$

```python
from math import pi

def spherical_volume(r):
    return (4/3) * pi * r**3
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 2. Observe or interpret values
* Packing rough gumball count of spheres related to 

```python
def gumball_capacity():
    d = dict()

    for r in range(4, 100+1):
        d[r] = int(spherical_volume(r) / spherical_volume(1))
    return d

for r, v in gumball_capacity().items():
    print(f'{r}: {v}')
```

Note that the number of gumballs that can be held in a sphere increases dramatically with the increase in volume of the sphere.

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
## 3. Answer questions

Write a function called `get_sphere()` that takes in a number of gumballs and returns the radius of sphere necessary to accommodate that inventory.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution

```python
def get_sphere(gumball_inventory):
    d = gumball_capacity()

    for k, v in d.items():
        if v > gumball_inventory:
            return k
    
    return 'No appropriate sphere available'
```
