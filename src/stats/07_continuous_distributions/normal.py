from math import e, pi, sqrt

def normal_pdf(x=0, mu=0, sigma=1):
    return (1 / (sigma * sqrt(2 * pi))) * e **(-(1/2) * ((x-mu) / sigma)**2)

print(normal_pdf(0.5, 0, 1))