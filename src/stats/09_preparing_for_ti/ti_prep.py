''' TI Style Questions (2029-01-21) '''

'''

TI Skills/Outline

* textbook problems re: Discrete Distrs and Probability
    * Recognize and solve problems related to:
        * Binomial
        * Poisson
        * Geometric
        * Uniform
        * Bayes Theorem

    * Understanding counting or binary through the lens of independent trials
        * binary ex: [0,1,1,0,1] <- each "coin flip or bit is independent of the other, if each bit is randomly generated"
        * trinary ex: [0, 1, 1, 2, 0]

    * Coding mathematical formulations

    * Analysis through Dictionaries
        * Pack values into dictionaries
            * Check membership vs not checking membership
        * Transform Dictionary values
        * General analytic approach
            * Create generative process
            * Load results into a dict
            * Interpret/Transform
'''



'''
You are sitting on a dock watching boats go by. On average, two out of every 13 boats that goes by has shipping containers on it. What is the probability that, in one particular set of observations, 10 out of 20 boats have shipping containers on them?
'''
from math import factorial, e

def combs(n,k):
    return factorial(n) / (factorial(n-k)* factorial(k))

def binomial_pmf(n,k,p):
    return combs(n,k)  *  p**k  * (1-p)**(n-k)

n = 20
k = 10
p = 2/13

# print(binomial_pmf(n,k,p))


'''
2 black cars go pass the stop sign every 15 minutes.

What is the proba that more than 10 black cars pass the stop sign in one hour?
'''
lmbda = 8


def poisson_pmf(lmbda, k):
    return e**(-lmbda) * lmbda**k / factorial(k)

def poisson_cdf(lmbda, k_high):
    accum = 0.0

    for k in range(0, k_high+1):
        accum += poisson_pmf(lmbda, k)
    return accum

# print(1 - poisson_cdf(lmbda, 10))

'''
A is the result of rolling a 4-sided die 5 times, and processing it through this function:


'''