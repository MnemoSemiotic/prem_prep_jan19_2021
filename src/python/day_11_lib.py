""" un/comment to de/activate ################

# project overview # stats_tools, binomial, poisson
# OOP (paradigm)
# encapsulates "state" and "logic"

# classes (objects)
class stats_tools:
    def factorial(n):
        prod = 1
        for i in range(1, n+1):
            prod *= i

        return prod


    def permutations(n, r):
        return int(stats_tools.factorial(n) / stats_tools.factorial(n - r))


    def combinations(n, r):
        return int(stats_tools.factorial(n) / (stats_tools.factorial(n - r) * stats_tools.factorial(r)))



# my_number = 4
# print( stats_tools.permutations(10, 2) ) # NameError: name 'factorial' is not defined

# functions vs methods
# classes vs formal OOP (object oriented programming)
# __dunder__ methods
# setting and mutating state


#####################################################################


class Binomial():
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.expected_value = n * p
        self.variance = self.expected_value * (1 - p)
        self.stdv = self.variance**(1/2)


    def __repr__(self):
        return f"Binomial| expected_value: {self.expected_value}"


    def new_n(self, nwn):
        self.__init__(nwn, self.p)


    def pmf(self, k):
        n = self.n
        p = self.p
        return stats_tools.combinations(n, k) * (p**k) * ((1 - p)**(n - k))


    def cdf(self, k):
        acc = 0
        for i in range(k+1):
            acc += self.pmf(i)

        return acc



# def binomial_pmf(n, p, k):
#     pass

# 10 flips P(X=7)
# ten_flips = Binomial(10, 0.5)
# print( ten_flips.n )
# print( ten_flips.stdv )

# ten_flips.new_n(1000)
# print( ten_flips.n )
# print( ten_flips.stdv )


#####################################################################

class Poisson():
    def __init__(self, lmbda):
        self.lmbda = lmbda
        self.expected_value = lmbda
        self.variance = lmbda
        self.stdv = lmbda**(1/2)


    def __repr__(self):
        return f"Poisson| lmbda: {self.lmbda}"


    def pmf(self, k):
        from math import e as E
        lmbda = self.lmbda
        return (E**(-lmbda)) * ((lmbda**k) / stats_tools.factorial(k))


    def cdf(self, k):
        acc = 0
        for i in range(k+1):
            acc += self.pmf(i)

        return acc


garden = Poisson(7)
print( garden.cdf(200) )

# <day_11_lib.Poisson object at 0x7fb903737700>

########################################## """
""" un/comment to de/activate ################

def squr_lst(lst):
    acc_lst = []
    for el in lst:
        try:
            acc_lst.append(el**2) # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
            print(d)

        except TypeError as err:
            print( f"warning {el} is a {type(el)} not an int" )

        except NameError as err:
            print( err )

    return acc_lst


print( squr_lst([4, 3, 5, "hello", 3.8, "hi"]) )
########################################## """
# """ un/comment to de/activate ################



########################################## """
