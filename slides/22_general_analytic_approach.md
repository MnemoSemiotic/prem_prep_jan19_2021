# General Analytic Approach
* Counting
* Sampling
* Closed Formula


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# A Simple, General Analytic Approach
Considering a stochastic process, model or create a sample space and analyze:
1. Synthesize outcomes, model a phenomenon, look at data
2. Observe values packed into a dictionary
3. Interpret or analyze



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

print(cards)
```