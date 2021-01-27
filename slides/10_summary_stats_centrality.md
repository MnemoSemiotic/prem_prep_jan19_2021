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

* Test with this data:

```python
a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]
```

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


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
* An article published in the journal, Indoor Air, considered two different air samples to test for endotoxin concentrations, the first in urban households, and the second in farmhouses.
    * Urban: 6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0
    * Farmhouse: 4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3
* A. Determine the sample mean for each group.

* B. Determine the trimmed mean for each group by trimming the smallest and largest value from each group.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
'''
A. Determine the sample mean for each group.
'''
urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

print(f'Sample Mean Urban: {round(mean(urban), 1)}')
print(f'Sample Mean Farmhouse: {round(mean(farmhouse), 1)}')

'''
B. Determine the trimmed mean for each group by trimming the smallest and largest value 
from each group.
'''
print(f'Sample Trimmed Mean Urban: {round(mean(urban, trim_by=1), 1)}')
print(f'Sample Trimmed Mean Farmhouse: {round(mean(farmhouse, trim_by=1), 1)}')

```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Median
* the middle value of a numeric data set

|Symbol                 |           Meaning               |
|-------------------------------|---------------------------------|
| <center>$med(A)$</center>        | Where A is the collection on which to take the median    |
| <center>$\tilde x$</center>| "x-tilde" is also used to represent median|


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Calculating Median
1. Sort the List
2. Find the middle value(s)
    * if list is odd, just select the middle value
    * if list is even, take mean of two middle values

* example:

```python
odd_list = [13, 18, 13, 14, 13, 16, 14, 21, 13]
even_list = [15, 14, 10, 8, 12, 8, 16, 13]
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (6 minutes)
* Code the `median()` function. Make sure to account for even and odd length lists.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def median(lst):
    lst_sorted = sorted(lst)

    # if odd
    if len(lst) % 2 == 1:
        mid = int(len(lst) / 2)
        return lst_sorted[mid]
    else:
        upper_mid_idx = int(len(lst)/2)
        return mean([lst_sorted[upper_mid_idx-1], lst_sorted[upper_mid_idx]])
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
An article published in the journal, Indoor Air, considered two different air samples to test for endotoxin concentrations, the first in urban households, and the second in farmhouses.

* Urban: 6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0
* Farmhouse: 4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0

Calculate the Median of both groups


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
urban = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0]

# print(sorted(urban))
# print(f'Median Urban: {round(median(urban), 1)}')
# print(sorted(farmhouse))
# print(f'Median Farmhouse: {round(median(farmhouse), 1)}')
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
An issue of a recent magazine reported the following home sale amounts for a sample of homes in Alameda, CA, all of which were sold in the previous month (1000s of $):

{ 590, 615, 575, 608, 350, 1285, 408, 540, 555, 679 }

a. Find the mean value of the homes sold in April

b. Find the median value of the homes sold in April 

Do you think mean or median is a “better” measure of center for this data? why? 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
An issue of a recent magazine reported the following home sale amounts for a sample of homes in Alameda, CA, all of which were sold in the previous month (1000s of $):

{ 590, 615, 575, 608, 350, 1285, 408, 540, 555, 679 }

a. Find the mean value of the homes sold in April
    * 620.5

b. Find the median value of the homes sold in April 
    * 582.5

c. Do you think mean or median is a “better” measure of center for this data? why? 
    * For this set of data, it’s likely that the median would be a more accurate summary statistic. This is due to outlier resistance


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Outlier Resistance
* The mean is not resistant to outliers, that is, the mean can be a misleading summary statistic if it is being greatly affected by a small number of outliers.

* The median is resistant to outliers, that is, the median is not affected by a small number of outliers, and is the superior measure of center when outliers are present.

* Choosing between mean and median can often be informed by the particular dataset which is being analyzed.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Mode
* Unlike the median and mean, the mode can be applied to categorical data.
    * Special Case: The median can be applied to categorical data which is ordinal in nature
* The mode is not very useful for continuous data. 
* Rather than trying to represent the “center” of a dataset or distribution, the mode seeks to find the element with the greatest frequency.
* Can consider first mode, second mode, and so on in describing a data set


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
Code the mode() function.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
'''
Mode
'''
def mode(lst):
    most_occurring = lst[0]

    for item in lst[1:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item

    return most_occurring


mode_lst = ['kangaroo', 'muskrat', 'platypus', 'muskrat', 'squid', 'squirrel', 'muskrat']

# print(mode(mode_lst))
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# A quick note on **sampling**
* A sample is comprised of materials selected from a **population**
* It's important to compose a sample that is **representative**
 