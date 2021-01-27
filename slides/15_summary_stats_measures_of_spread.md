* Add [this Chrome Extension](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima) so you can see math equations rendered in GitHub

# Summary Stats: Measures of Spread
* Five Number Summary
* IQR (InterQuartile Range)
* Determining Outliers
* Variance
* Standard Deviation




<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Five-Number Summary
* The five number summary gives a more in depth description of a numerical collection
    * The Minimum
    * Q1 - The first quartile or the 25th percentile
    * The Median
    * Q3 - The third quartile or the 75th percentile
    * The Maximum



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (5 minutes)
* Code the `five_number_summary()` function



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def five_number_summary(lst):
    min_ = min(lst)
    max_ = max(lst)
    med = median(lst)

    sorted_lst = sorted(lst)

    if len(lst) % 2 == 1:
        lower_half = sorted_lst[0: int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2)+1: ]
    else:
        lower_half = sorted_lst[0: int(len(lst) / 2)]
        upper_half = sorted_lst[int(len(lst) / 2): ]

    q1 = median(lower_half)
    q3 = median(upper_half)

    return min_, q1, med, q3, max_
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (2 minutes)

```python
a = [15,2,9,5,6,7,27,12,18,19,1]
b = [6,1,4,51,7,16,10,14,46,22,24,56,48,54]
```

* Calculate the 5 number summary
* What is the mean?
* What is the best measure of centrality for this data?

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
a = [15,2,9,5,6,7,27,12,18,19,1]
b = [6,1,4,51,7,16,10,14,46,22,24,56,48,54]
```

```python
print(sorted(a))
print(five_number_summary(a))
print(mean(a))
print(median(a))
print('\n')
print(sorted(b))
print(five_number_summary(b))
print(mean(b))
print(median(b))
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Interquartile Range (IQR)
* Using Q1 and Q3 we can determine the interquartile range (IQR)
    * IQR = Q3 - Q1
* The interquartile range can be used to qualify outliers




<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Code the `iqr()` function

* show the 5 number summary and IQR of `a` and `b`

```python
a = list(range(0, 50+1, 5)) 
b = list(range(0, 100+1, 5))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def iqr(lst):
    _, q1, _, q3, _ = five_number_summary(lst)
    return q3 - q1

a = list(range(0, 50+1, 5)) 
b = list(range(0, 100+1, 5))

print(a)
print(five_number_summary(a))
print(iqr(a))

print(b)
print(five_number_summary(b))
print(iqr(b))
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Determining Outliers
* If a value is less than 1.5 * IQR below Q1, or is greater than $1.5 \times IQR$ above Q3 it can be classified as an outlier. 


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 Minutes)
Code the `detect_outliers()` function together
* BONUS: Include a variable multiplier for the IQR, so that you can set outliers different from $1.5 \times IQR$, such as $1.75 \times IQR$, etc.


```python
def detect_outliers(lst, outlier_coef=1.5):
    pass
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def detect_outliers(lst, outlier_coef=1.5):
    '''
    given a list of data points, return a list containing
    the detectuble outliers
    '''
    _, q1, _, q3, _ = five_number_summary(lst)
    iqr_ = iqr(lst)

    outliers = []

    for num in lst:
        if num < q1 - outlier_coef*iqr_:
            outliers.append(num)

        if num > q3 + outlier_coef*iqr_:
            outliers.append(num)

    return outliers

test_outliers = list(range(0,100))
test_outliers.append(10_000)

print(detect_outliers(test_outliers, outlier_coef=1.5))

```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Consider the dataset from the previous question:

```python
a = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]
```

A. Calculate the five number summary for the data
    (mean) = 620.5, median = 582.5

B. Determine the IQR of the Dataset

C. Determine whether any of the data points can be defined as outliers. If so, what are the outliers?

D. What is the best measure of centrality for this data?



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
Consider the dataset from the previous question:

```python
a = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]
```

```python
a =  [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]
# print(sorted(a))

'''Calculate the five number summary for the data
(mean) = 620.5, median = 582.5'''

'''Determine the IQR of the Dataset'''
# print('iqr', iqr(a))

'''Determine whether any of the data points can be defined as outliers. If so, what are the outliers?
'''
# print('outliers: ',detect_outliers(a))

'''What is the best measure of centrality for this data?'''

```

D. What is the best measure of centrality for this data?



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
* Write a function called `remove_outliers` that takes a `list` as input and returns a new `list` with all values that are not outliers


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def remove_outliers(lst, outlier_coef=1.5):
    outliers = detect_outliers(lst, outlier_coef)
    output = []

    for num in lst:
        if num not in outliers:
            output.append(num)
    
    return output

a =  [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

print(remove_outliers(house_prices))
```



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Variance

* Much like measures of center, the “spread,” or variance of a distribution can be informative, and help us describe the distribution.
* Average squared distance between each data point and the mean
* Notation
    * $s^2$ : refers to the variance of a sample
    * $\sigma^2$ : refers to the variance of a population
* The square root of the variance is the **Standard Deviation**
    * $s$ : refers to the standard deviation of a sample
    * $\sigma$: refers to the standard deviation of a population

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Variance Formula
* Average squared distance between each data point and the mean

* **Population Variance**:

$$
\sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2
$$

* **Sample Variance**:

$$
\sigma^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline x)^2
$$

* Recall:
    * $\mu$ : population mean
    * $\overline x$ : sample mean


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Bessel's Correction for Sample Variance
* Makes the assumption that any given sample is more likely to exclude some values which live in the upper or lower extremes of a population. A smaller denominator will lead to a larger coefficient, and therefore a larger variance which is likely to be closer to the population’s true variance.
* 