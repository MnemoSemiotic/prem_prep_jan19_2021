* Add [this Chrome Extension](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima) so you can see math equations rendered in GitHub



# Statistics: Measures of Centrality
* Why Statistics?
* Measures of Centrality

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Why are probability and statistics important?
* Data Science is an extension of statistics, just as it is an abstraction of all the Sciences
* **All** of our models and practices in data science are either rooted in or validated by probability and statistics
    * Experimental design and reporting are performed through the lens of statistics
    * Linear Regression, Logistic Regression
    * Sampling/Resampling Methods (Bootstrap)
    * confidence intervals
    * expectation, deviance, etc

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Statistics vs Machine Learning vs Artificial Intelligence

![ds comic](images/statsvsmlvsai.jpeg)


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Basic Summary Statistics Overview
* Measures of Central Tendency
    * Mean
    * Median
    * Mode
* Measures of variance or “spread”
    * Variance
    * Standard Deviation


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Mean
* sum of the numeric elements, divided by the number of elements, expressed as:

$$
\frac{1}{n} \sum_{i=1}^n a_i
$$

|Symbol                 |           Meaning               |
|-------------------------------|---------------------------------|
| <center>$\mu$</center>        | lowercase greek mu refers to **population mean**    |
| <center>$\overline x$</center>| "x-bar" refers to the **sample mean** |
| <center>$\overline X$</center>| capital "X-bar" refers to the sample mean where $\bold X$ is a random variable |



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Trimmed Mean
* Can be used to combat large devations and outliers
* “trim” some percent off of  max and min of data list:
* Advantage - can help combat outliers that might influence our mean
* Disadvantage - we are removing portions of our data which might be very important



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
*  Code the `mean()` function
* BONUS: Include a `trim` parameter that removes the greatest and least `n` values

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def mean(lst, trim_by=0):
    lst_ = lst.copy()

    if trim_by > 0:
        
        lst_ = sorted(lst_)[trim_by:-trim_by]

    return sum(lst_) / len(lst_)
```
