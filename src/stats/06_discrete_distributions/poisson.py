from math import factorial, e


def poisson_pmf(lmbda, k):
    return e**(-lmbda) * lmbda**k / factorial(k)


print(poisson_pmf(0.125, 0.125))
