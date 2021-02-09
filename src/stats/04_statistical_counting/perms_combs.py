def factorial(n):
    prod = 1

    for num in range(2, n+1):
        prod *= num

    return prod

# print(factorial(5))
# print(factorial(0))


