from math import factorial, e


def poisson_pmf(lmbda, k):
    return e**(-lmbda) * lmbda**k / factorial(k)


# print(poisson_pmf(10, 10))
