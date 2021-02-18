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