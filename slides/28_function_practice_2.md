<!-- https://docs.google.com/presentation/d/1mU6T1oNXZp-neU7lPcZRWZGHgdVcR9e7VNW4q8gypnA/edit#slide=id.p -->

<!-- 1 -->
# Function Practice 2!

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 2 -->
## Function Breakout # 1

Remember coding the PMF for our binomial distribution, let's now create a function that will return our CDF for a binomial distribution
A problem for CDF might look like:
Suppose you have a fair coin and you flip it 10 times, what is the probability that there will be 6 or more heads as a result of these 10 flips?


We want to represent the below equation in python, where n is the number of trials, k is the number of successes and p is the probability of a success.
<br><img src="images/formula_binomial_cdf.png"
         alt="Binomial CDF Formula"
         width="300"
         />

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 3 -->
Suppose you have a fair coin and you flip it 10 times, what is the probability that there will be 6 or more heads as a result of these 10 flips?


So let's think about this problem first. Let's say a success = heads, so what do we need in order to perform this problem?
<br><img src="images/formula_binomial_cdf.png"
         alt="Binomial CDF Formula"
         width="300"
         />

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 4 -->
Let's take a step back and think about in general how can we code our CDF? Without the context of a problem prompt


What code have we created that can help us with creating our CDF code?
We have already created the PMF code, so we can reuse this in our CDF code!

```python
def binomial_pmf(n, k, p = 0.5):
   return combination(n, k) * (p ** k) * ((1 - p)**(n-k))
```

<br><img src="images/formula_binomial_cdf.png"
         alt="Binomial CDF Formula"
         width="300"
         />

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 5 -->
Step 1: Based on our code how can we modify? Let's take
this step by step
When you look at this equation:
And you see that summation, what does this remind you of?

An integer/float accumulator!

<br><img src="images/formula_binomial_cdf.png"
         alt="Binomial CDF Formula"
         width="300"
         />

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 6 -->
Step 2: How do we iterate to accumulate? What does our loop look like?
```python
cdf_probs = 0
for i in range(k+1):
    cdf_probs += ???
```

<br><img src="images/formula_binomial_cdf.png"
         alt="Binomial CDF Formula"
         width="300"
         />

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 7 -->
Step 3: What is the value that we need to add to our accumulator for each iteration?

Think about the code you already have at your disposal!

```python
cdf_probs = 0
for i in range(k+1):
    cdf_probs += binomial_pmf(n, i, p = 0.5)
```
<br><img src="images/formula_binomial_cdf.png"
         alt="Binomial CDF Formula"
         width="300"
         />

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 8 -->
### Step 4: Let's put it all together and wrap it in a function called `binomial_cdf()`

```python
def factorial(n):
   fact = 1
   for i in range(1, n + 1):
      fact *= i
   return fact

def combination(n, k):
   return int(factorial(n) / (factorial(n - k)* factorial(k)))

def binomial_pmf(n, k, p = 0.5):
  return combination(n, k) * (p ** k) * ((1 - p)**(n-k))

def binomial_cdf(n, k, p = 0.5):
   cdf_probs = 0
   for i in range(k+1):
       cdf_probs += binomial_pmf(n, i, p)
   return cdf_probs
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 9 -->
Now let's revisit our problem we started with:
Suppose you have a fair coin and you flip it 10 times, what is the probability that there will be 6 or more heads as a result of these 10 flips?
What would be our answer for this? Remember what the question is asking for!
First call our binomial_cdf function like so:
\
`binomial_cdf(10, 5)`\
This gives us the probability that we will have 5 or less, but we want the probability of 6 or more, what do we need to do now?
\
`1 - binomial_cdf(10, 5) = 0.3769`\


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 10 -->
Now let's revisit our problem we started with:
Suppose you have a fair coin and you flip it 10 times, what is the probability that there will be 6 or more heads as a result of these 10 flips?
Conversely we can look at the problem like this:
```python
binomial_pmf(10, 6)  +
binomial_pmf(10, 7)  +
binomial_pmf(10, 8)  +
binomial_pmf(10, 9)  +
binomial_pmf(10, 10) = 0.3769
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 11 -->
Let's use our functions we have created to see if we can answer the following problems
An article “Should you report that fender bender?” from Consumer Reports in Sept 2013 reported that 7 in 10 auto accidents involve a single vehicle (disclaimer: the article recommends that any accident involving more than one vehicle should always be reported). Suppose 15 accidents are randomly selected. Show me how you would call your function **to get the answer**

* What is the probability that exactly 4 of the 15 randomly selected accidents involve only one vehicle?
<!-- `binomial_pmf(15, 4, 0.7) = ??` -->
<!-- 0.0005805753776550008 -->

* What is the probability that fewer than 4 of the 15 randomly selected accidents only involve one vehicle
<!-- `binomial_cdf(15, 3, 0.7) = ??` -->
<!-- 9.165869215200015e-05 -->

* What is the probability that 10 or more randomly selected accidents only involved one vehicle?
<!-- `1 - binomial_cdf(15, 9, 0.7)= ??` -->
<!-- 0.7216214402043639 -->

* What is the probability that more than 5 and less than 8 of the 15 randomly selected accident involved only one vehicle?
<!-- `binomial_pmf(15, 6, 0.7) + binomial_pmf(15, 7, 0.7) = ??` -->
<!-- 0.04636001904534003 -->
<!-- lwr = 5
upr = 8
print( binomial_cdf(15, upr-1, 0.7) - binomial_cdf(15, lwr, 0.7) ) #  -->

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 12 -->
## Function Breakout # 2
Changing gears here, let's create a function that takes in a list of words and returns a new list of words that are anagrams of each other:
Example:
This list:\
`['dog', 'god', 'cat', 'act', 'tack', 'star', 'rat', 'rats']`

Will return:\
`['dog', 'god', 'cat', 'act', 'star', 'rats']`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 13 -->
Step 1: Think about the problem, how do we approach this? What are we comparing and how to we compare it?

We are comparing each item in the list to every other item in the list EXCEPT itself!

But what does this look like?

We will need two for loops!s


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 14 -->
Step 2: Before we get into our iteration structure, let's think about what the comparisons that we need to make are

Let's take the words 'dog' and 'god' for example, are these anagrams of each other?

So how can we compare these two words??

`sorted('dog') == sorted('god')`

Why doesn't this work?
`set('dog') == set('god')`
Think about
`set('dog') == set('good')`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 15 -->

Step 2: Let’s think about our accumulator, what are we accumulating into?

`anagram_lst = []`

Step 3: What does our control flow look like, just use i and j for to represent our words

`if sorted(i) == sorted(j):`


Step 4: How do we add our accumulation into this control flow?

```python
if sorted(i) == sorted(j):
    anagram_lst.append(????)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 16 -->
Step 5: What are we appending to our accumulator?

```python
if sorted(i) == sorted(j):
    anagram_lst.append(i)
```
Step 6: Let’s think about our edge cases here. What might those be?

>Think about if you are comparing each item in the list
to each item in the list again


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 17 -->
Step 6 continued: so how do we take care of those edge cases in our control flow?
```python
if i == j:
    continue
elif sorted(i) == sorted(j):
    anagram_lst.append(i)

# Or

if sorted(i) == sorted(j) and i != j:
    anagram_lst.append(i)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 18 -->
Step 7: How do we write code to compare everything in the list to itself? How many loops might we need?

```python
for i in lst:
    for j in lst:
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 19 -->

Step 8: Let’s put the code we have come up with so far together and wrap it in a function called `anagrams()`
```python
def anagrams(lst):
anagram_lst = []
for i in lst:
        for j in lst:
if sorted(i) == sorted(j) and i != j:
                anagram_lst.append(i)
    return anagram_lst

Try running the code with the list:
l = ['dog', 'god', 'cat', 'act', 'tack', 'star', 'rat', 'rats',
    'arts', 'start', 'good']
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 20 -->
What’s wrong with our output?? How do we change our code to
get exactly what we want?

```python
def anagrams(lst):
anagram_lst = []
for i in lst:
        for j in lst:
if sorted(i) == sorted(j) and i != j:
                anagram_lst.append(i)
    return list(set(anagram_lst))

# OR

def anagrams(lst):
anagram_lst = set()
for i in lst:
        for j in lst:
if sorted(i) == sorted(j) and i != j:
                anagram_lst.add(i)
    return list(anagram_lst)
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 21 -->
## Function Breakout # 3

Let’s create a function that sorts a given string, where each word in the string will contain a single number. This number is the position the word should have in the result.
Numbers can be from 1 to 9, so the first word will have a 1 not a 0 in it.
If the string is empty, return an empty string, and the words in the input string will only contain valid consecutive numbers

Examples:
```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```
Codewars kata: https://www.codewars.com/kata/55c45be3b2079eccff00010f/python


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 22 -->
Step 1: Let’s think about how we want to approach this problem. If we are given a string like this\
`"4of Fo1r pe6ople g3ood th5e the2"`

In words, explain how you would approach this problem.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 23 -->
Step 2: Let’s first think about our edge case, If the string is empty, return an empty string.

How would we code this?

```python
if sentence == '':
   return ''
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 24 -->

Step 3: So let’s first split up our text into words, how can we analyze our words to get our words in the order we might want them to be in? Or how can we label our words with number that is in our word?
If i give you this code, what would you do next?\
`for word in sentence.split():`

Right now we are iterating over each word, so how can we get the number inside that word?
```python
for word in sentence.split():
   for char in word:
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 25 -->
Step 3: So let’s first split up our text into words, how can we analyze our words to get our words in the order we might want them to be in? Or how can we label our words with number that is in our word?
```python
for word in sentence.split():
    for char in word:
```
What do we need to do to get our number out?
```python
for word in sentence.split():
    for char in word:
        if char.isdigit():
```
This will allow us to check if that character is non alpha, so now let’s think about what we want and how we want to accumulate it.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 26 -->
Step 3: So let’s first split up our text into words, how can we analyze our words to get our words in the order we might want them to be in? Or how can we label our words with number that is in our word?
```python
d = [] # accumulate into a list using tuples
   for word in sentence.split():
       for char in word:
           if char.isdigit():
                    d.append(char, word)
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 27 -->
Step 4: Now that we have a list of tuples, what do we need to do with this list to get the words out in the order we want them to be in?
Let’s say this is what our accumulated list of tuples looks like
`[(2, 'is2'), (1, 'Thi1s'), (4, 'T4est'), (3, '3a')]`

One cool thing is if you call sorted() on your list of tuples, it will sort on your 0-index item within each tuple from smallest to largest. Let’s try it out

`d = sorted([(2, 'is2'), (1, 'Thi1s'), (4, 'T4est'), (3, '3a')])`

`[(1, 'Thi1s'), (2, 'is2'), (3, '3a'), (4, 'T4est')]`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 28 -->
Step 5: Now that we have a sorted list of tuples, what do we need to do with this list to get the words out in a string? What does our accumulator look like?

`[(1, 'Thi1s'), (2, 'is2'), (3, '3a'), (4, 'T4est')]`

`s = ''`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 29 -->
Step 6: Now that we have a sorted list of tuples, what do we need to do with this list to get the words out in a string? What does our iterator look like and how are we adding to our accumulator?
```python
[(1, 'Thi1s'), (2, 'is2'), (3, '3a'), (4, 'T4est')]

s = ''
   for i in sorted(d):
       s += i[1]
    return s
```
What’s wrong with the above code??


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 30 -->
```python

[(1, 'Thi1s'), (2, 'is2'), (3, '3a'), (4, 'T4est')]

s = ''
   for i in sorted(d):
       s += i[1]
    return s
```
This will return: `'Thi1sis23aT4est'`


So how do we fix it?

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 31 -->
```python
[(1, 'Thi1s'), (2, 'is2'), (3, '3a'), (4, 'T4est')]

s = ''
   for i in sorted(d):
       s += i[1] + ' '
    return s
```
This will return: `'Thi1s is2 3a T4est '`

How can we remove the trailing white space?


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 32 -->
```python
[(1, 'Thi1s'), (2, 'is2'), (3, '3a'), (4, 'T4est')]

s = ''
   for i in sorted(d):
       s += i[1] + ' '
    return s.strip()  
```
This will return: `'Thi1s is2 3a T4est'`

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 33 -->
Step 7:  Let’s put it all together in a function called order()
```python
def order(sentence):
   if sentence == '':
       return ''
   d = []
   for i in sentence.split():
       for c in i:
           if c.isdigit():
               d.append( (int(c), i) )
   s = ''
   for i in sorted(d):
       s += i[1] + ' '
   return s.strip()
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 34 -->

Note there are definitely more pythonic ways to approach this problem, I just wanted you to understand how to see a prompt like this and solve through it step by step to get to the answer. You can always iterate and clean your code once you have a working answer!

Try it with these sentences
`"cal8l lo6ng 2about mak3e fe4el 1be 5and t7ake"`

`"public1 9own lif8e 3a hav5e n6umber ot7her 4government be2"`

`"man6 1seem to4 fe5w p2roblem an3d"`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------

<!-- 35 -->
## Homework

https://colab.research.google.com/drive/1xoEV7vTms1Q6UMzxNum9Q2SinAnVpw9L

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
