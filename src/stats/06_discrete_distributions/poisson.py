from math import factorial, e


def poisson_pmf(lmbda, k):
    return e**(-lmbda) * lmbda**k / factorial(k)


# print(poisson_pmf(10, 10))


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)



lmbda = 10
k = 10

for n in range(k, 10000):
    print(f'binom: {round(binomial_pmf(n, k, p=(lmbda/n)), 7)}')
    print(f'poiss: {round(poisson_pmf(lmbda, k), 7)}')
    print()


