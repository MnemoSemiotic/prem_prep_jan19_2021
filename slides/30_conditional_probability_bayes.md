# Conditional Probability and Bayes
* Bayesian vs Frequentist Thought
* Kolmogorov's Definition for Conditional Probability
* Law of Total Probability
* Bayes Theorem
* Bayes Textbook Problems


<br><br><br><br><br><br><br>

----------------------------------------------------
# Bayesian vs Frequentist Thought
##### Frequentist
Statistical inference in the past century has primarily relied upon a classical, or frequentist approach, which makes inferences about populations from samples. This approach results in some explicit level of confidence via hypothesis testing and confidence intervals, using probability theory and probability distributions as the foundation to determine whether a sampling is difference by chance, or because the population being sampled is actually different than some initial hypothesized value.

##### Bayesian
ayesian Inference does not consist of a static model the way that frequentist statistics do, rather, the models take in new information, and based on that new data, the underlying probabilistic model is adjusted. This is called the posterior distribution, in the end we end up with an evolving model. Essentially, new observations allow for “updating a belief” about the phenomenon being observed.


<br><br><br><br><br><br><br>

----------------------------------------------------
# Conditional Probability
A conditional probability is a measure of the probability of one event occurring, given that another (different) event has occurred, or will occur.
* Implicitly, we presume, assume, assert, or see evidence that the given event has or will occur.
* This can be interpreted as limiting the sample space of the event we are measuring. 


<br><br><br><br><br><br><br>

----------------------------------------------------
# Visualizing Conditional Probability

![cond proba visual](images/venn_diagram_cond_proba.png)

$$
P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{2}{2+3} = \frac{2}{5} = 0.4
$$


<br><br><br><br><br><br><br>

----------------------------------------------------
# Kolmogorov's Definition
### of Conditional Probability

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$


<br><br><br><br><br><br><br>

----------------------------------------------------
# Conditional Probability Example

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

A survey was given to a number of regarding their pets. 40% of respondents reported owning a dog, 45% of respondents reported owning a cat, and 25% of students responded to owning both (All students owning both were counted in all categories). 

##### What is the probability of a student owning a dog, if we know they own a cat?

1. Frame the question

$$
P(\text{cat}|\text{dog}) = ?
$$

2. Write down known info
* $P(\text{cat})$
* $P(\text{dog})$
* $P(\text{cat} \cap \text{dog})$