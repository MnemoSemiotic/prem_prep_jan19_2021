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
$$
P(k events) = \frac{e^{-\lambda}\lambda^k}{k!}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Poisson Example Problems

**Example 1**
On average, ten people visit the ATM in an hour. What is the probability that 12 people visit the ATM in an hour?

$\lambda = 10$
$k = 12$

$$
P(k \text{ events} ) = \frac{e^{-10} \cdot 10^{12}}{12!} = 0.0948
$$
