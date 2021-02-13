
def geometric_pmf(p, k, inclusive=True):
    return p * (1-p)**(k-inclusive)
    # if inclusive:
    #     return p * (1-p)**(k-1)
    # else:
    #     return p * (1-p)**(k)



'''
You are flipping a fair coin. What is the probability that
you get your first heads on the 7th flip?
'''
p = 0.5
k = 7

# print(geometric_pmf(p, k, inclusive=True))
# print(geometric_pmf(p, k-1, inclusive=False))



'''
You have a series of routers transmitting packets of data. There is a 0.99 probability that a given packet of data passes through the router.

What is the probability that a given packet of data is lost in the 15th router?
'''

p = 0.01
k = 15

# print(geometric_pmf(p, k, inclusive=True))
# print(geometric_pmf(p, k-1, inclusive=False))


def geom_cdf_accum(p, k, inclusive=True):
    proba = 0.0

    for r in range(inclusive, k+1):
        proba += geometric_pmf(p, r, inclusive)
    
    return proba

def geom_cdf_closed(p, k, inclusive=True):
    return 1 - (1-p)**(k +(not inclusive))
    
    # if inclusive:
    #     return 1 - (1-p)**k
    # else:
    #     return 1 - (1-p)**(k+1)


p = 0.05
k = 10

# print(geom_cdf_accum(p, k, inclusive=True))
# print(geom_cdf_accum(p, k-1, inclusive=False))

# print(geom_cdf_closed(p, k, inclusive=True))
# print(geom_cdf_closed(p, k-1, inclusive=False))


'''
You have a series of routers transmitting packets of data. There is a 0.99 probability that a given packet of data passes through the router.
'''

'''
What is the probability that a given packet of data will pass successfully through 14 routers?
'''
# print(0.99**14)

'''
What is the probability that a given packet will be dropped before the 15th router it passes through... in other words, on or before the 14th router.
'''
p = 0.01
# print(geom_cdf_closed(p, 14, inclusive=True))


def geometric_pmf_dict(p, k_high, inclusive=True):
    d = dict()

    for k in range(inclusive, k_high+1):
        d[k] = geometric_pmf(p, k, inclusive)

    return d

d_incl = geometric_pmf_dict(p=0.05, k_high=10, inclusive=True)
d_excl = geometric_pmf_dict(p=0.05, k_high=10, inclusive=False)

for k, v in d_incl.items():
    print(f'{k}: {v}')