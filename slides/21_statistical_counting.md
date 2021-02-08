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