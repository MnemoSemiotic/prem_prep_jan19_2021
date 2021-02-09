from math import factorial

def factorial(n):
    prod = 1

    for num in range(2, n+1):
        prod *= num

    return prod

# def factorial(x): 
#     if x == 1: return x 
#     else: return x * factorial(x-1)

# print(factorial(5))
# print(factorial(0))


'''
There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?

Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?
'''
# print(factorial(10))
# card_S = factorial(10)
# card_A = 1
# print(card_A / card_S)


