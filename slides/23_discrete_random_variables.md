# Discrete Random Variables
* Discrete vs Continuous
* Defining a Random Variable
* Probability Mass Function (PMF)
* Cumulative Density Function (CDF)


<br><br><br><br><br><br><br><br><br><br><br><br><br>
-----------------------------------------
# Recall: Discrete vs Continuous
**Discrete**: countable outcomes
* "discretized": there is nothing inbetween two given values

**Continuous**: can be thought of in terms of measurement
* "infinite precision": if we have a powerful enough tool for measurement, then no two item measurements would be equal
* Can discretize continous values by collecting them into bins of defined ranges


<br><br><br><br><br><br><br><br><br><br><br><br><br>
-----------------------------------------
# Defining a Random Variable (rv)
A Random Variable can be thought of as a well-defined "view" onto a stochastic (random) facet of a phenomenon. We can then ask probabilistic questions regarding specific potential values of that random variable.

**Example:**
Let the random variable $X$ represent the count of 1's in a base-3 number of length 3. 

Sample space of $X$:

All possible length 3 trinary outcomes
```
000 001 002 010 011 012 020 021 022
100 101 102 110 111 112 120 121 122
200 201 202 210 211 212 220 221 222
```

Corresponding values of $X$
```
  0   1   0   1   2   1   0   1   0
  1   2   1   2   3   2   1   2   1
  0   1   0   1   2   1   0   1   0
```

What is the the probability that $X$ will equal 3?
$P(X=3) = ?$
* Count the number of occurrences of 3, divide by the total number of outcomes

$P(X=3) = \frac{1}{27}$