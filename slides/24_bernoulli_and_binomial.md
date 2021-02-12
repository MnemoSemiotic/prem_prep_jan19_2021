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


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Understanding the Binomial Distribution
## Through Counting

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Counting in Binary
* Can think of binary, initially, as a 2 symbol translation from our well-known decimal system
* 2 symbols in binary: [0, 1]

Decimal to Binary relationship in 2-bit binary:

```
DEC  BIN
0:    0
1:    1
```

Decimal to Binary relationship in 2-bit binary:

```
DEC  BIN
0:    00
1:    01
2:    10
3:    11
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Counting in Binary cont'd

Decimal to Binary relationship in 3-bit binary:

```
DEC   BIN
0:    000
1:    001
2:    010
3:    011
4:    100
5:    101
6:    110
7:    111
```

Decimal to Binary relationship in 4-bit binary:

```
DEC    BIN      DEC   BIN
0:    0000       8:   1000
1:    0001       9:   1001
2:    0010      10:   1010
3:    0011      11:   1011
4:    0100      12:   1100
5:    0101      13:   1101
6:    0110      14:   1110
7:    0111      15:   1111
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Place values in Binary

Consider the Binary word
10110110

This can be broken down into place values

|128's place|64's|32's|16's|8's|4's|2's|1's|
|---------------|--------------|-------------|-------------|------------|------------|-------------|--------------|
|      1        |             0|            1|            1|           0|           1|            1|             0|
| $1 \cdot 128$ | $0 \cdot 64$ | $1 \cdot 32$| $1 \cdot 16$| $0 \cdot 8$| $1 \cdot 4$|  $1 \cdot 2$|   $0 \cdot 1$|
| 128 +       |         0 +    | 32 +        | 16 +        | 0 +        | 4 +        |  2 +        |    0         |

$128 + 0 + 32 + 16 + 0 + 4 + 2 + 0 = 182$

Thus:
|  BIN    |    DEC  |
|---------|---------|
|10110110 |    182  |

### What is the maximum decimal value we can represent in 8-bit binary?

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Simple Code to Count in 4-bit Binary

```python
def gen_4_bit_binary():
    bin_dct = dict()
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_dct[decimal] = [i,j,k,l]
                    decimal += 1
    return bin_dct

for dec, bin_ in gen_4_bit_binary().items():
    print(f'{dec}: {bin_}')
```

But, what if we want to count arbitrarily high values in Binary corresponding to some Decimal value?

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Decimal to Binary Algorithm

```
Given a decimal number
    - take the modulus by 2
        - set aside the result
    - floor divide the number by 2
        - until that number is 0
    - reverse the sequence of outcomes
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Decimal to Binary Algorithm Example

```
dec_to_bin(43)
--------------
43 % 2     ==> 1
43 // 2 = 21
21 % 2     ==> 1
21 // 2 = 10
10 % 2     ==> 0
10 // 2 = 5
5 % 2      ==> 1
5 // 2  = 2
2 % 2      ==> 0
2 // 2  = 1
1 % 2      ==> 1
1 // 2  = 0

reversed ==> 101011 is the binary representation of 43
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (6 minutes)

Code the `dec_to_bin` function
Should take as input 2 things:
* a decimal value (dec)
* a number of bits (n_bits=8)


Algorithm:
```
Given a decimal number
    - take the modulus by 2
        - set aside the result
    - floor divide the number by 2
        - until that number is 0
    - reverse the sequence of outcomes
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (6 minutes)

Code the `dec_to_bin` function

```python
def dec_to_bin(dec, n_bits=8):
    bin_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2

    return bin_list[::-1] # list(reversed(bin_list))
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Building a DEC to BIN table
Can collect values into a dictionary

```python
def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)

    return bins_d

for dec, bin_ in get_binary(n_bits=8).items():
    print(f'{dec}: {bin_}')
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Why Binary?
#### We can think of a binary number (word) as being a series of successes and failures

```
1 1 0 0
S S F F
```

#### The count of 1's in 4-bit binary will follow a binomial distribution, with a probability of $0.5$ per trial

```
0: *            0: 1/16
1: ****         1: 4/16
2: ******       2: 6/16
3: ****         3: 4/16
4: *            4: 1/16
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Construct Binomial for $n$ trials with $p=0.5$
* Using a Counting approach
* Note that, in this binary approach, we are "stuck with" probability per trial of $0.5$

```python
def binomial_distr(n_trials=8):
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, val in bin_dict.items():
        sum_bits = sum(val)
        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1

    return binomial_dict

d = binomial_distr(n_trials=12)

# for the counts
for k, v in d.items():
    print(f'{k}: {v}')

# for the probabilities
for k, v in d.items():
    print(f'{k}: {round(v / sum(d.values()), 5)}')
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)

You flip a coin 12 times. 
* $n$ is the number of Bernoulli trials
* $k$ is the number of successes for which we want the probability
* $p$ is the probability of success on any given trial

#### What is the probability that you get 9 heads in 12 flips?
* What are the values for $n$, $k$, and $p$



#### What is the probability of getting 4 or less heads in 12 flips?
* What are the values for $n$, $k$, and $p$

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution

You flip a coin 12 times. 
* $n$ is the number of Bernoulli trials
* $k$ is the number of successes for which we want the probability
* $p$ is the probability of success on any given trial

#### What is the probability that you get 9 heads in 12 flips?
* What are the values for $n$, $k$, and $p$
    * $n=12$
    * $k=9$
    * $p=0.5$
    * $P(X=9) = 0.05371$

#### What is the probability of getting 4 or less heads in 12 flips?
* What are the values for $n$, $k$, and $p$
    * $n=$
    * $k=$
    * $p=$
    * $P(X \le 4) = P(X=0) + P(X=1) + P(X=2) + P(X=3) + P(X=4) = 0.19384$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Understanding the Binomial Distribution
## Through Sampling


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Constructing Binomial with a fixed $p$
### using `choice`

```python
from random import choice

def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    return [get_bit() for _ in range(n)]
    # lst = []
    # for _ in range(n):
    #     lst.append(get_bit())
    # return lst
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
#### Write a function called binary_sampling_dict that has two params
* `num_bits=8`
* `num_samples=1000`

return a `dict` where the keys represent the number of successes,
and the values associated with those keys represent the count
of that number of successes occurring.

```python
{
    0: 35,
    1: 63,
    ...
    num_bits: count of num_bits successes
}

# 00101101 : 4 successes
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
#### Write a function called binary_sampling_dict that has two params
* `num_bits=8`
* `num_samples=1000`

```python
def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        observed_k = sum(binary)

        if observed_k not in d:
            d[observed_k] = 0
        d[observed_k] += 1

    return d
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (3 minutes)
Run the code below and describe the difference in outcomes between the 2 resulting dictionaries:

```python
''' one trial of 100 samples '''
d1 = binary_sampling_dict(num_bits=16, num_samples=100)

for k, v in sorted(d1.items()):
    print(f'{k}: {v / sum(d1.values)}')


''' one trial of 1000 samples '''
d2 = binary_sampling_dict(num_bits=16, num_samples=1000)

for k, v in sorted(d2.items()):
    print(f'{k}: {v / sum(d2.values)}')
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
Descriptions here will vary. The main thing to observe is that the greater the `num_samples`, the more confidence we will have in the resulting probabilities for each value of `k`


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Running more trials of samples
#### will get us closer and closer to the theoretical distribution we encountered via counting

```python

''' 500 trials of 1000 samples '''
def binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict(n_bits, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)

    return d_out

d = binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500)

# observing counts
for k, v in sorted(d.items()):
    print(f'{k}: {v}')

observing probabilities
for k, v in sorted(d.items()):
    print(f'{k}: {v / sum(d.values())}') # averaged (observed) probability

```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Variable $p$ in Binomial sampling approach
#### Using `random()`, we can change our $p$ value

```python
def get_success(p=0.5):
    if random() < p:
        return 1
    else:
        return 0

print(get_success(0.25))

def generate_n_successes(n=8, p=0.5):
    lst = []
    for _ in range(n):
        lst.append(get_success(p))
    return lst

print(generate_n_successes(n=8, p=0.05))

# verify, as 12*0.25 = 3
test_trials = 100000
trial_results = []
for _ in range(test_trials):
    trial_results.append(generate_n_successes(12, p=0.25).count(1))

print(sum(trial_results) / test_trials)
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Observing Binomial with different $p$ values


```python
def binary_sampling_vary_p(num_bits=8, p=0.5, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_successes(num_bits, p)
        k = sum(binary)

        if k not in d:
            d[k] = 0
        d[k] += 1

    return d


''' One trial of 1000 samples '''
d = binary_sampling_vary_p(num_bits=8, p=0.3, num_samples=1000)

for k, v in sorted(d.items()):
    print(f'{k}: {v}')

''' 500 trials of 1000 samples '''

def binary_sampling_clt_vary_p(n_bits=8, p=0.5, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_vary_p(n_bits, p, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)
    
    return d_out

''' 500 trials of 1000 samples '''

d = binary_sampling_clt_vary_p(n_bits=8, p=0.3, num_samples=1000, num_sample_trials=500)

for k, v in sorted(d.items()):
    print(f'{k}: {v}')
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Understanding the Binomial Distribution
## via the PMF


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Binomial Probability Mass Function (PMF)

$$
P(X=k) = {n \choose k} p^k(1-p)^{n-k}
$$

$n$ = number of bernoulli trials
$p$ = probability of success on any given bernoulli trial
$k$ = specific number of successes for which to find the probability

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Other parameters of the Binomial Distribution
$n$ = number of bernoulli trials
$p$ = probability of success on any given bernoulli trial
$k$ = specific number of successes for which to find the probability

$$
P(X=k) = {n \choose k} p^k(1-p)^{n-k}
$$

Mean or Expected Value

$$
E[X] = np
$$

Variance 

$$
Var(X) = np(1-p)
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Reading Notation

#### X~binomial(n, p)
is read as "The random variable X follows a binomial distribution with n trials and probability p per trial"


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
#### Code the Components of the Binomial PMF
* `factorial()`
* `combinations`

recall the Combinations formula

$$
nCk = \frac{n!}{(n-k)!k!}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution

```python
def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (3 minutes)
#### Why do you think combinations is part of the Binomial PMF?


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
Essentially there are multiple ways to arrange successes over a series of bernoulli trials. However, the arrangement of those successes is irrelevant. Thus the presence of combinations handles the different ways that $k$ successes can occur over $n$ trials.

Different ways to arrange 3 successes over 8 trials
```
00000111
01010100
10000101
etc...
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (3 minutes)
### Code the Binomial PMF (`binomial_pmf(n,p,k)`)
* 3 parameters
$n$ = number of bernoulli trials
$p$ = probability of success on any given bernoulli trial
$k$ = specific number of successes for which to find the probability

$$
P(X=k) = {n \choose k} p^k(1-p)^{n-k}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
### Code the Binomial Distribution 

```python
def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
#### Solve these 3 Binomial PMF problems


##### What is the probability in 12 coin flips of a fair coin, that you get 7 heads?

n = ?
k = ?
p = ?


##### Sitting on a park bench you observe geese walking by. There's a probability of 0.3 that any goose walking by has black feet. What is the probability that 4 out of the next 12 geese walking by has black feet?

n = ?
k = ?
p = ?



##### At the cat cafe, there is a 40% chance that any one cat you see is a Siberian.  What is the probability that 6 out of the 14 cats at the park are Siberian?

n = ?
k = ?
p = ?



<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
#### Solve these 3 Binomial PMF problems


##### What is the probability in 12 coin flips of a fair coin, that you get 7 heads?

```python
n = 12
k = 7
p = 0.5

print(binomial_pmf(n, k, p)) # --> 0.1934
```

##### Sitting on a park bench you observe geese walking by. There's a probability of 0.3 that any goose walking by has black feet. What is the probability that 4 out of the next 15 geese walking by has black feet?

```python
n = 15
k = 4
p = 0.3

print(binomial_pmf(n, k, p)) # --> 0.2187
```

##### At the cat cafe, there is a 40% chance that any one dog you see is a Siberian.  What is the probability that 6 out of the 14 dogs at the park are Siberian?

```python
n = 14
k = 6
p = 0.4

print(binomial_pmf(n, k, p)) # --> 0.2066
```



<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Binomial Cumulative Distribution Function (CDF)
Note that this is an accumulator pattern

$$
P(X \le k) = \sum_{i=0}^k {n \choose i}p^i(1-p)^{n-i}
$$

For example, flipping a fair coin 9 times, what is the probability that there will be 4 or fewer heads?

$$
P(X \le 4) = P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4)
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes) 
### Code the Binomial CDF (`binomial_pmf(n,p,k_high)`)

$$
P(X \le k) = \sum_{i=0}^k {n \choose i}p^i(1-p)^{n-i}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
### Code the Binomial CDF (`binomial_pmf(n, k_high, p=0.5)`)

```python
def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0.0

    for k in range(0, k_high+1):
        cumulative += binomial_pmf(n, k, p)

    return cumulative
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (3 minutes)
#### Solve this Binomial CDF problem

There are 8 components in parallel and functioning independent of each other. At least 3 of those components need to be operational for a given circuit to function. The probability of any given component being operational upon observation is 0.7. What is the probability that at least 3 components are operational upon observation?



<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (3 minutes)
#### Solve this Binomial CDF problem

There are 8 components in parallel and functioning independent of each other. At least 3 of those components need to be operational for a given circuit to function. The probability of any given component being operational upon observation is 0.7. What is the probability that at least 3 components are operational upon observation?

```python
print(1 - binomial_cdf(8, 2, 0.7))
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT
#### Code the `binomial_pmf_dict()` function.
This should take 4 parameters:
* `n`: the number of trials
* `k_low`: the low value of $k$ in the dictionary
* `k_high`: the high value of $k$ in the dictionary
* `p=0.5`: the probability of success of a given bernoulli trial


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution

```python
def binomial_pmf_dict(n, k_low, k_high, p=0.5):
    d = dict()

    for k in range(k_low, k_high+1):
        d[k] = binomial_pmf(n, k, p)

    return d

d = binomial_pmf_dict(8, 0, 8, p=0.25)

for k, v in d.items():
    print(f'{k}: {v}')
```



<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# Consider the `binomial_cdf_dict()` function

```python
def binomial_cdf_dict(n, k_low, k_high, p=0.5):
    d = dict()

    for k in range(k_low, k_high+1):
        d[k] = binomial_cdf(n, k, p)

    return d

d = binomial_cdf_dict(8, 0, 8, p=0.25)

for k, v in d.items():
    print(f'{k}: {v}')
```