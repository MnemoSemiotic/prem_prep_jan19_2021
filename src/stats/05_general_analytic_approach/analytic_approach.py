

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


# for outcome in S:
#     print(outcome)

# print(len(S))


'''
breakout solution
'''

hits = []
range_to_hit = 18

for outcome in S:
    if outcome[0] >= range_to_hit and outcome[2].count('H') == 2:
        hits.append(outcome)

# print(f'proba: {round(len(hits) / len(S), 3)}')



'''
Random Sampling
'''
from random import choice

def num_attendees():
    num_peeps = 1

    for _ in range(20):
        num_peeps += choice(range(0, 11+1))

    return num_peeps

print(num_attendees())