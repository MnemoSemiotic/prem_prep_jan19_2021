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
* $P(\text{cat}) = 0.45$
* $P(\text{dog}) = 0.40$
* $P(\text{cat} \cap \text{dog}) = 0.25$

3. Apply Kolmogorov's Definition

$$
P(A|B) = \frac{P(A \cap B)}{P(B)} \\
$$

$$
P(\text{cat}|\text{dog}) = \frac{P(\text{cat} \cap \text{dog})}{P(\text{dog})}
$$

$$
= \frac{0.25}{0.45}
$$

$$
P(\text{cat}|\text{dog}) = 0.55
$$

Thus the probability of a student owning a cat given that they own a dog is **0.55**


<br><br><br><br><br><br><br>

----------------------------------------------------
# Independence and Dependence
#### by Kolmogorov's Definition
By rearranging the definition, we can qualify independence of a probability problem. 

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

**Dependence**
if 

$$
P(A \cap B) = P(A|B) \times P(B)
$$

then the events have dependency

**Independence**
if 

$$
P(A \cap B) = P(A) \times P(B)
$$

then the events are independent. Notice how this recalls the **Multiplication Rule** for independent events.


<br><br><br><br><br><br><br>

----------------------------------------------------
# Breakout (3 minutes)
$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

A survey of 400 vehicles was taken driving on an afternoon, the survey found that 175 of the vehicles were red, 120 of the vehicles were trucks, and 37 of the vehicles were red trucks. 

##### Given that a random truck is chosen, what is the probability that it is red?

##### Given that a random red vehicle is chosen, what is the probability that it is a truck?


<br><br><br><br><br><br><br>

----------------------------------------------------
# Breakout Solution

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

##### Given that a random truck is chosen, what is the probability that it is red?

$P(A) = P(Red) = \frac{175}{400} = 0.4375$

$P(B) = P(Truck) = \frac{120}{400} = 0.300$

$P(A \cap B) = P(\text{Red} \cap \text{Truck}) = \frac{37}{400} = .0925$

$P(\text{Red}|\text{Truck}) = \frac{P(\text{Red} \cap \text{Truck})}{P(\text{Truck})} = \frac{0.0925}{0.3} = 0.3083$

##### Given that a random red vehicle is chosen, what is the probability that it is a truck?

$P(\text{Truck} | \text{Red}) = \frac{P(\text{Red} \cap \text{Truck})}{\text{Red}} = \frac{0.0925}{0.4375} = 0.2114$


<br><br><br><br><br><br><br>

----------------------------------------------------
# Law of Total Probability
Given a sample space which is divided into a number of disjoint events, an overlapping event can be interpreted as the aggregation of that event in each subspace.

![](images/venn_diagram_law_of_total_proba.png)

Here, $A$ can be represented as:

$$
A = (B1 \cap A)  \cup   (B2 \cap A)  \cup   (B3 \cap A)
$$


<br><br><br><br><br><br>

----------------------------------------------------
# Applying Kolmogorov 
By rearranging

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

to

$$
P(A \cap B) = P(A|B) \times P(B)
$$

we can rewrite

$$
A = (B1 \cap A)  \cup   (B2 \cap A)  \cup   (B3 \cap A)
$$

as

$$
P(A) = P(A|B1)P(B1)  +   P(A|B2)P(B2)  +   P(A|B3)P(B3)
$$



<br><br><br><br><br><br>

----------------------------------------------------
# 