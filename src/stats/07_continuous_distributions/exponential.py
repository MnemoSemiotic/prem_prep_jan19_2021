from math import e, sqrt

 def exponential_pdf(lmbda, x):
     if x < 0: return 0
     return lmbda * e**(-lmbda * x)

