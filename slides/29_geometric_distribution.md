# Geometric Distribution
* Using the PMF
* Sampling


<br><br><br><br><br><br><br><br>

--------------------------------
# Geometric Probability Distribution
* Similar to binomial, but with no fixed value for $n$ 
* Represents a sequence of identical bernoulli trials before the first success

Example: We can apply the geometric PMF to determine the probability of having to flip a fair coin 5 times before a flip resulting in “heads” on the 6th flip


<br><br><br><br><br><br><br><br>

--------------------------------
# Geometric PMF: 2 forms
The two forms of the Geometric Probability Mass Function can be used to express the same problem. One just includes the first success in its calculation

* PMF calculating the number of trials up to **and including** the first success

$$
P(X=k) = p (1-p)^{k-1}
$$

* PMF calculating the number of trials **before** the first success

$$
P(X=k) = p (1-p)^{k}
$$


<br><br><br><br><br><br><br><br>

--------------------------------
# Geometric Mean

##### Mean / Expectation up to **and including** the first success

$$
E(X) = \frac{1}{p}
$$

##### Mean / Expectation **before** the first success

$$
E(X) = \frac{1-p}{p}
$$


<br><br><br><br><br><br><br><br>

--------------------------------
# Geometric Variance
No difference in these two forms

##### Variance (up to **and including** the first success)

$$
Var(X) = \frac{1-p}{p^2}
$$

##### Variance (**before** the first success)

$$
Var(X) = \frac{1-p}{p^2}
$$


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT (4 minutes)
Code the `geometric_pmf()` function
* `p` : probability
* `k` : number of failures (inclusive or exclusive of the 1st success)
* `inclusive=True` : whether or not to use inclusive or exclusive pmf

PMF calculating the number of trials up to **and including** the first success

$$
P(X=k) = p (1-p)^{k-1}
$$

PMF calculating the number of trials **before** the first success

$$
P(X=k) = p (1-p)^{k}
$$

<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT Solution
Code the `geometric_pmf()` function
* `p` : probability
* `k` : number of failures (inclusive or exclusive of the 1st success)
* `inclusive=True` : whether or not to use inclusive or exclusive pmf

```python
def geometric_pmf(p, k, inclusive=True):
    return p * (1-p)**(k-inclusive)
    # if inclusive:
    #     return p * (1-p)**(k-1)
    # else:
    #     return p * (1-p)**k
```


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT (2 minutes)


You are flipping a fair coin. What is the probability that
you get your first heads on the 7th flip?

p = ?
k = ?


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT Solution

You are flipping a fair coin. What is the probability that
you get your first heads on the 7th flip?

```python
p = 0.5
k = 7

print(geometric_pmf(p, k, inclusive=True))
print(geometric_pmf(p, k-1, inclusive=False))
```

<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT (2 minutes)

You have a series of routers transmitting packets of data. There is a 0.99 probability that a given packet of data passes through the router.

What is the probability that a given packet of data is lost in the 15th router?


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT Solution

You have a series of routers transmitting packets of data. There is a 0.99 probability that a given packet of data passes through the router.

What is the probability that a given packet of data is lost in the 15th router?

```python
p = 0.01
k_inclusive = 15
k_exclusive = 14

print(geometric_pmf(p, k_inclusive, inclusive=True))
print(geometric_pmf(p, k_exclusive, inclusive=False))
```


<br><br><br><br><br><br><br><br>

--------------------------------
# Geometric CDF
Note that we have convenient closed formulas for the CDF

* CDF for the number of trials up to **and including** the first success

$$
P(X \le k) = 1 - (1-p)^{k}
$$

* CDF for the number of trials **before** the first success

$$
P(X \lt k) = 1 - (1-p)^{k+1}
$$


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT (5 minutes)
Code 2 Functions

`geom_cdf_accum(p, k, inclusive=True)`
This function should use the PMF functions in an accumulator pattern


`geom_cdf_closed(p, k, inclusive=True)`
This function should use the CDF formulas: 
* up to **and including** the first success
    * $P(X \le k) = 1 - (1-p)^{k}$
* **before** the first success
    * $P(X \lt k) = 1 - (1-p)^{k+1}$


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT Solution

```python
def geom_cdf_accum(p, k, inclusive=True):
    proba = 0.0

    if inclusive:
        starting_at = 1
    else:
        starting_at = 0

    for r in range(starting_at, k+1):
        proba += geometric_pmf(p, r, inclusive)

    return proba


def geom_cdf_closed(p, k, inclusive=True):
    if inclusive:
        return 1 - (1-p)**k
    else:
        return 1 - (1-p)**(k+1)
```