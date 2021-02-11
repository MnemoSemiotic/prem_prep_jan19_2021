from random import random

def bernoulli(p_success=0.5):
    draw = random()

    if draw < p_success:
        return True
    else:
        return False

# print(bernoulli(p_success=0.3))


# trials = 10000000
# print([bernoulli(p_success=0.3) for _ in range(trials)].count(True) / trials)


