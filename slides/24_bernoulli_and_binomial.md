# Bernoulli and Binomial
* Discrete Probability Distributions
* Discrete Uniform Distributions
* Uniform Distribution
* Bernoulli Trial
* Counting in Binary
* Binomial Distribution
    * Counting
    * Sampling
    * Using the PMF



<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Probability Distributions
Recall: A Random Variable (RV) can generally be thought of as representing the potential outcomes of a random experiment.

The frequency of occurrences of outcomes of a Random Variable can be thought of as a **Probability Distribution**. Note that a Probability Distribution is dependant on the definition of the RV.


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Discrete Probability Distribution
In this course we will consider four discrete probability distributions, in addition to the novel ones we define.

**Uniform Distribution**
For a given range of discrete outcomes, every outcome has equal probability. For example, a single fair die roll will have equal probability for any given side.

**Bernoulli Trial**
The result of an experiment with two mutually exclusive outcomes, commonly thought of as Failure or Success, with a parameter $p$ representing the probability of success.

**Binomial Distribution**
Represents the number of successes in a series of $n$ Bernoulli Trials with a fixed probability $p$

**Poisson Distribution**
Given an average frequency per span of time, area, or volume, referred to as lambda ($\lambda$), represents the probabilities of different numbers of events, given constraints of independence of events and identical distribution of events.

**Geometric Distribution**
Represents the number of Failures in Bernoulli Trials up to the First success. The probability $p$ for each Bernoulli trial is held constant.


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Uniform Distribution
Every outcome is discrete and has equal probability.

When rolling a 32 sided die, the probability of getting any one outcome is $\frac{1}{32}$. The probability of getting less than or equal to a given outcome is $P(X \le x) = \sum \frac{1}{32} \cdot x$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Bernoulli Trial
A bernoulli trial is a single event with a binary outcome and set probability of success $p$.

Example:
If you have a bag full of red and blue balls, where you have 30 red balls, and 70 blue. 

If you reach into the bag thousands of times and average the counts of these balls what percentage would you expect of your draws would be red?

What is the $P(Red)$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
Code the `bernoulli()` function. It should take one argument, `p_success`.

You will want to use `from random import random`. The `random()` function will return a uniformly distributed random float between 0 and 1.


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
Code the `bernoulli()` function. It should take one argument, `p_success`.

```python
def bernoulli(p_success=0.5):
    draw = random() # gets a val betw 0 and 1

    if draw < p_success:
        return True
    else:
        return False
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Let's verify the prior Breakout
By sampling a high number of times from the `bernoulli()` function, we should approach the value of $p$, by way of dividing the number of successes by the number of samples taken.

```python
trials = 10000000
print([bernoulli(p_success=0.5) for _ in range(trials)].count(True) / trials)

# in other words
true_count = 0
for _ in range(trials):
    if bernoulli(p_success=0.5) == True:
        true_count += 1

print(true_count / trials)
```