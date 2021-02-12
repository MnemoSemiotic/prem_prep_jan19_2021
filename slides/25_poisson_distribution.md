# Poisson Distribution
* Poisson Phenomena
* Poisson PMF
* Relationship with Binomial


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# The Poisson Distribution

The Poisson Probability Distribution represents the number of events occuring in a given interval of time or space
* $\lambda$ represents the typical or expected frequency in a given interval

**Constraints:**
1. The rate represented by lambda is constant
2. Each “success” or event is independent, discrete, and random
3. Two events cannot occur at the exact same instant


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# The Poisson Probability Mass Function (PMF)
* Given a typical frequency, $\lambda$, find the probability for a specific number of outcomes $k$
* $\lambda$ can be adapted to different sizes of interval
* The PMF provides the 

$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Poisson Example Problems

$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$

**Example 1**
On average, ten people visit the ATM in an hour. What is the probability that 12 people visit the ATM in an hour?

$\lambda = 10$
$k = 12$

$$
P(\lambda=10, k=12) = \frac{e^{-10} \cdot 10^{12}}{12!} = 0.0948
$$

Thus the probability of 12 people visiting the ATM in an hour is 0.0948.


**Example 2**
A specific space telescope takes random images of deep space. On average 23 Super Giant stars are seen in an image. What is the probability that two randomly selected images will have a total count of 35 Super Giant stars in them?

$\lambda = 23 * 2$
$k = 35$

$$
P(\lambda=46, k=35) = \frac{e^{-46} \cdot 46^{35}}{35!} = 0.01602
$$

Thus the probability of seeing 35 stars in two images is 0.01602.


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
Code the `poisson_pmf()` function.
Note, both the constant `e` and the `factorial()` function are available from the `math` module.


$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$

