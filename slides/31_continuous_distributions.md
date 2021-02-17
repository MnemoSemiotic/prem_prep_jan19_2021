# Continuous Distributions
* Continuous Random Variables
* Uniform Continuous
* Exponential
* Normal


<br><br><br><br><br><br><br><br>

--------------------------------------
# Continuous Random Variables
* Methods for determining expected values typically depend on the application of calculus (integration)
* Probabilities of continuous random variables are represented by Probability Density Functions (PDF) 


<br><br><br><br><br><br><br><br>

----------------------------------------
# PDF vs PMF
* A PMF is able to produce probabilities for distinct values in the range
* A PDF does not give probabilities for distinct values, it produces probabilities over a given interval.


<br><br><br><br><br><br><br><br>

----------------------------------------
# Zero probability
In a continuous distribution, the probability of a single, exact outcome will be 0

Instead, we search for the probability within a range

$$
P(a \le x \le b)
$$

<br><br><br><br><br><br><br><br>

----------------------------------------
# Area under the Curve
The probability of a range of outcomes can be represented as the area under the curve for the plot of a probabilistic function.
* recall: $P(A) = \frac{|A|}{|S|}$

Can perform **integration** for integrable functions

Can apply Riehmann Sums approach for non-integrable functions


<br><br><br><br><br><br><br><br>

----------------------------------------
# Continuous Distributions
##### Uniform Continuous Distribution
Between some range, all values have equal probability

##### Exponential Distribution
Related to the Poisson distribution; where the Poisson distribution models “events per time (or area),” the exponential measure time (or space) in between events. Commonly used to model waiting times	

##### Normal Distribution
Normally distributed random variables have the iconic “bell-shaped” curve. 


<br><br><br><br><br><br><br><br>

----------------------------------------
# Uniform Continuous
Consider a uniform continuous distribution between $0$ and $1$. 

The probability of drawing a random value less than $0.43$ can be expressed as

$$
P(x \lt 0.43) = \frac{0.43 - 0}{1.0 - 0.0}
$$

$$
P(x \lt 0.43) = 0.43
$$

NOTE: due to the infinite precision of a continuous distribution, $\lt$ and $\le$ are equivalent above.



<br><br><br><br><br><br><br><br>

----------------------------------------
# Uniform Params

##### Expected Value

$$
E = \frac{1}{2}(\text{low bound} + \text{high bound})
$$

##### Variance

$$
\sigma^2 = \frac{1}{12}(\text{high bound} - \text{low bound})^2
$$

<br><br><br><br><br><br><br><br>

----------------------------------------
## Constructing a Uniform Continuous Distribution
Applying geometric decay to a binomial process

```python
from random import choice

def get_bit():
    return choice([0,1])


def get_binary(n=8):
    return [get_bit() for _ in range(n)]

    # return_list = []

    # for _ in range(n):
    #     return_list.append(get_bit())

    # return return_list

# print(get_binary(16))

def get_float(n=8):
    bin_list = get_binary(n)

    float_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5**idx

    return float_accum, bin_list


print(get_float(8))
```


<br><br><br><br><br><br><br><br>

----------------------------------------
# Exponential Distribution
Where the Poisson distribution models “events per time (or area),” exponential measures time (or space) between Poisson events. 
* The most common application is to model waiting times	
    * The time necessary to wait for a cab
    * The time waiting to see the next shooting star while stargazing
    * Waiting time for the next customer to arrive at a store

----------------------------------------
# BREAKOUT (5 Minutes)
##### Code these 5 Exponential Functions

|                                                                      | |                         |
|----------------------------------------------------------------------|-|-------------------------|
|**Exponential ($\lambda$) PDF**                                       | |**Exponential Mean**      |
|`exponential_pdf(lmbda, x):`                                          | |`exponential_mean(lmbda):`|
|$f(x) = \lambda e^{-\lambda x} \text{ for } x \ge 0, \text{ else } 0$ | |<center>$E(X) = \frac{1}{\lambda}$</center>|

|                                                                 | |                              |
|-----------------------------------------------------------------|-|-----------------------------|
|**Exponential ($\lambda$) CDF**                                  | |**Exponential Variance**      |
|`exponential_cdf(lmbda, x):`                                     | |`exponential_variance(lmbda):`|
|$f(x) = 1 - e^{-\lambda x} \text{ for } x \ge 0, \text{ else } 0$| |<center>$E(X) = \frac{1}{\lambda^2}$</center>|

Also code `exponential_std(lmbda)`

----------------------------------------
# BREAKOUT Solution

```python
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
```
