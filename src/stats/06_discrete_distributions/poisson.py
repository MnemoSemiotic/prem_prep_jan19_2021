from math import factorial, e


def poisson_pmf(lmbda, k):
    return e**(-lmbda) * lmbda**k / factorial(k)


# print(poisson_pmf(10, 10))


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)



lmbda = 20
k = 10

# for n in range(k, 10000):
#     print(f'binom: {round(binomial_pmf(n, k, p=(lmbda/n)), 7)}')
#     print(f'poiss: {round(poisson_pmf(lmbda, k), 7)}')
#     print()





'''
Phenomenon:
Cars passing by an intersection at a certain time of day/year, for the duration of a fixed amount of time, will likely follow a Poisson distribution

Question:
A given intersection will have, on avg, 15 cars pass through in 10 minutes. What is the probability that 20 cars pass through in 15 minutes?
'''
lmbda = 15 * (15/10)
k = 20

# print(poisson_pmf(lmbda, k)) # -> 0.0769



def poisson_cdf(lmbda, k_high):
    cdf = 0.0

    for k in range(k_high+1):
        cdf += poisson_pmf(lmbda, k)
    
    return cdf

print(poisson_cdf(10, 10))