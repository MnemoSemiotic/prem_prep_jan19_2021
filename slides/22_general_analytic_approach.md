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
    if outcome[0] >= range_to_hit and outcome[2].count('H') >= 2:
        hits.append(outcome)

print(f'Proba of hit: {round((len(hits)/len(S)),3)}') #--> 0.264
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Random Sampling Example
* Can be used to approach a theoretical distribution and estimate parameters of that distribution

Consider invitations for a small party you want to have with two of your friends. You let them know that they can each invite one more person. They in term let those friends that they 



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 1. Synthesize outcomes, model a phenomenon, look at data


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 2. Observe or interpret values


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
## 3. Answer questions
