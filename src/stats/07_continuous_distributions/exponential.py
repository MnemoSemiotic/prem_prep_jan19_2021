from math import e, sqrt


def exponential_pdf(lmbda, x):
    if x < 0: return 0
    return lmbda * e**(-lmbda * x)


def exponential_cdf(lmbda, x):
    if x < 0: return 0
    return 1 - e**(-lmbda * x)


def exponential_mean(lmbda):
    return 1 / lmbda


def exponential_variance(lmbda):
    return 1 / lmbda**2


def exponential_std(lmbda):
    return sqrt(exponential_variance(lmbda))



'''
Suppose you’re on a street corner trying to hail a taxi cab. Let

X = The amount of time (in minutes) that you have to wait.
X ~ exponential(0.1)
ƛ = 0.1 (meaning the rate of cab arrivals is 0.1 per minute)
'''

lmbda = 0.1

# What’s the probability that you’ll have to wait more than ten minutes?
print(1 - exponential_cdf(lmbda, x=10))

# What is the amount of time that you would expect to wait?


# What is the variance of this random variable?