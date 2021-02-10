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


<br><br><br><br><br><br><br><br><br><br><br><br><br>
-----------------------------------------
# Example 1:
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


<br><br><br><br><br><br><br><br><br><br><br><br><br>
-----------------------------------------
# Example 2:
NOTE: Using the same phenomenon, we can define a different RV

Let the random variable $Y$ represent whether a 2 is present in a base-3 number of length 3. 
* $Y = 0$  if no $2$ is present
* $Y = 1$  if $2$ is present

Sample space of $Y$:

All possible length 3 trinary outcomes
```
000 001 002 010 011 012 020 021 022
100 101 102 110 111 112 120 121 122
200 201 202 210 211 212 220 221 222
```

Corresponding values of $X$
```
  0   0   1   0   0   1   1   1   1
  0   0   1   0   0   1   1   1   1
  1   1   1   1   1   1   1   1   1
```

What is the the probability that $Y$ will equal 1?
$P(Y=1) = ?$
* Count the number of occurrences of 1, divide by the total number of outcomes

$P(Y=1) = \frac{19}{27}$


<br><br><br><br><br><br><br><br><br><br><br><br><br>
-----------------------------------------
# Probability Mass Function (PMF)
The above example probability questions are of the PMF Type. 

A PMF describes the probability that a discrete random variable is equal to a certain value, and is written in the form:

$P(X=x)$, where $X$ represents the random variable, and $x$ represents a specific outcome of that random variable.