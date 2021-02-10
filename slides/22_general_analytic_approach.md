# General Analytic Approach
* Counting
* Sampling
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

1. Synthesize Outcomes by counting

```python
rolls = range(1,36+1)
suits = ['Spades ','Clubs','Diamonds','Hearts']
card_nums = ['Ace', 'One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']

cards = []

for suit in suits:
    for card in card_nums:
        cards.append(f'{card} of {suit}')

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

2. Observe/Interpret values in a list

```python

for 
```