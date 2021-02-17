""" un/comment to de/activate ################

# factorial
def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i

    return prod


# print(factorial(4))
# print(factorial(5))


# combinations n! / (n-r)! * r!
def combinations(n, r):
    return int(factorial(n) / ( factorial(n - r) * factorial(r) ))


# print( combinations(10, 2) )


# binomial_pmf
def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1 - p)**(n - k))


# print( binomial_pmf(10, 4) )
# print( binomial_pmf(10, 5) )
# print( binomial_pmf(10, 6) )


# binomial_cdf
def binomial_cdf(n, k, p=0.5):
    acc = 0
    for i in range(0, k+1):
        acc += binomial_pmf(n, i, p)

    return acc


# print( binomial_cdf(10, 6) )
# print( binomial_cdf(10, 10) ) # 1
# print( binomial_cdf(10, 10) - binomial_cdf(10, 5) )

########################################## """
""" un/comment to de/activate ################

'''

7 in 10 auto accidents involve a single vehicle.
p = 0.7

Suppose 15 accidents are randomly selected.
n = 15

what is our success case?
an accident involves only 1 vehicle

'''
What is the probability that exactly 4 of the 15 randomly selected accidents involve only one vehicle?
print( binomial_pmf(15, 4, 0.7) ) # 0.0005805753776550008

What is the probability that fewer than 4 of the 15 randomly selected accidents only involve one vehicle
print( binomial_cdf(15, 3, 0.7) ) # 9.165869215200015e-05

What is the probability that 10 or more randomly selected accidents only involved one vehicle?
print( 1 - binomial_cdf(15, 9, 0.7) ) # 0.7216214402043639

What is the probability that more than 5 and less than 8 of the 15 randomly selected accident involved only one vehicle?
print( binomial_pmf(15, 6, 0.7) + binomial_pmf(15, 7, 0.7) ) # 0.04636001904534003

# lwr = 5
# upr = 8
# print( binomial_cdf(15, upr-1, 0.7) - binomial_cdf(15, lwr, 0.7) ) # 0.04636001904534003

########################################## """
""" un/comment to de/activate ################

def anagrams(lst):
    anag_lst = []
    for word1 in lst:
        for word2 in lst:
            if word1 != word2 \
            and sorted(word1) == sorted(word2) \
            and word1 not in anag_lst:
                anag_lst.append(word1)

    return anag_lst


my_lst = ['dog', 'god', 'dog', 'cat', 'act', 'tack', 'tack', 'star', 'rat', 'rats']
print( anagrams(my_lst) )
# ['dog', 'god', 'cat', 'act', 'star', 'rats']

# word1 and word2 can't be the same word
# have to have the same letters
    # compare the sorted versions of each word


########################################## """
""" un/comment to de/activate ################
def order(txt):
    tup_lst = []
    for word in txt.split():
        for ch in word:
            if ch.isdigit():
                tup_lst.append(  (int(ch), word)  )
                break

    lst = []
    for num, word in sorted(tup_lst):
        lst.append(word)

    return " ".join(lst)


print(order("is2 Thi1s T4est 3a"))
          # "Thi1s is2 3a T4est"
print(order("4of Fo1r pe6ople g3ood th5e the2" ))
          # "Fo1r the2 g3ood 4of th5e pe6ople"
print(order("")) # ""

# print(sorted( [(2, 'is2'), (1, 'Thi1s'), (4, 'T4est'), (3, '3a')] ))

########################################## """
