# Statistical counting
* Factorial
* Permutations
* Combinations


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Factorial: $n!$
*  Can be thought of as the cardinality, or number of ways, that $n$ items can be arranged.
    * Ex: $9!=9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1=362880$
    * Note: $0!=1$, as there is only one way to arrange zero items.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Factorial and selecting without replacement
Consider selecting 3 numbered balls from an urn, without replacement:
* In the first selection, there are 3 choices
* In the second selection, there are 2 choices
* In the thrid selection, there is 1 choice

Possible Sequences:

| Selection One | Selection Two | Selection Three|
|---------------|---------------|----------------|
|  <center>1</center> | <center>2</center> | <center>3</center>|
|  <center>1</center> | <center>3</center> | <center>2</center>|
|  <center>2</center> | <center>1</center> | <center>3</center>|
|  <center>2</center> | <center>3</center> | <center>1</center>|
|  <center>3</center> | <center>1</center> | <center>2</center>|
|  <center>3</center> | <center>2</center> | <center>1</center>|


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes) code `factorial()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution

```python
def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)

There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?


Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution

There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?
* Solution: $10! = 10 \times 9 \times 8 \times 7 \times 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 3628800$


Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?
* Solution: $\frac{1}{3628800} \approx .0000003$


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Permutations: $nPk = \frac{n!}{(n-k)!}$
* A **permutation** can be thought of as an arrangement of a number of items
* $nPk$
    * where $n$ is the number of possible items
    * $k$ is how many of those items to arrange
* Note: **ORDER MATTERS**


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# Permutations: Discovery by Counting
$nPk = \frac{n!}{(n-k)!}$

If we consider $n$ to be the base of a counting system, then we can determine all permutations $k$ by a counting/reduction approach.

1. Count in base $n$ system
* ex: $n=3$

000 010 020 100 110 120 200 210 220
001 011 021 101 111 121 201 211 221
002 012 022 102 112 122 202 212 222
                            
2. Reduce counts that have duplicate items

000 010 020 100 110 **120** 200 **210** 220
001 011 **021** 101 111 121 **201** 211 221
002 **012** 022 **102** 112 122 202 212 222

3. Consider $k$ items

ex: $k=3$
<b>012
021
102
120
201
210
</b>