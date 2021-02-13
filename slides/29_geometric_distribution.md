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


