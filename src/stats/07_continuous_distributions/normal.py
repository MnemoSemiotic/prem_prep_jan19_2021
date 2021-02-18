from math import e, pi, sqrt

def normal_pdf(x=0, mu=0, sigma=1):
    return (1 / (sigma * sqrt(2 * pi))) * e **(-(1/2) * ((x-mu) / sigma)**2)

# print(normal_pdf(0.5, 0, 1))


def normal_cdf(x=0, mu=0, sigma=1):
    x_vals = [num*0.001 for num in range(-1000, int(x*1000))]
    accum = 0.0

    for val in x_vals:
        accum += normal_pdf(val, mu, sigma)
        if val > x:
            break

    return accum * 0.001


# print(normal_cdf(x=300, mu=475, sigma=98)) # 0.0370


'''
A radar unit is used to measure speeds of cars on a motorway. The speeds are normally distributed with a mean of 90 km/hr and a standard deviation of 10 km/hr. What is the probability that a car picked at random is travelling at more than 100 km/hr?
'''
mu = 90
sigma = 10
x = 100
print(1 - normal_cdf(x, mu, sigma))