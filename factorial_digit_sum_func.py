# ref.: https://www.python-course.eu/recursive_functions.php

# A fuction that return fatorial of the number specified in paramaters of the function
def factorial(n):
    # factorial of 0! is true to be 1 
    # print("factorial has been called with n = " + str(n))
    if n == 0:
        return 1
    else:
        res = n * factorial(n-1) 
        # technique of recursion, i.e., call of the function inside itself
        # print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

#print(factorial(10))

def sum_nums_of_factorial(n):
    return str(factorial(n))

print(sum_nums_of_factorial(10))




    