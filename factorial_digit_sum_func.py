# A script that calculates the sum of numbers a factorial number is made up of
# ref.: https://www.python-course.eu/recursive_functions.php

# A fuction that return fatorial of the number specified in paramaters of the function
def factorial(n):
    # factorial of 0! is true to be 1 
    #print("factorial has been called with n = " + str(n))
    if n == 0:
        return 1
    else:
        res = n * factorial(n-1) 
        # technique of recursion, i.e., call of the function inside itself
        #print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

# function that return sum of numbers a factorial number is made up of
def calc_nums_sum_of_factorial(n):
    numList = [] # list to store each number of a factorial individually
    # we can cast a returning integer of factorial(n) function to a string
    # now we can itterate this string and append each character to a list
    for num in str(factorial(n)):
        # append to a list and cast an individual string number back to integer, making it list of ints
        numList.append(int(num)) 
    print("List of numbers of a factorial -> " + str(numList))
    # once the list is ready, we can pass it to another function that will calculate sum
    # of numbers in the list. 
    return calc_nums_sum_from_list(numList)

# calculates a sum of numbers from the list. 
def calc_nums_sum_from_list(numList):
    sum = 0
    for num in numList:
        sum += num
    return sum

# returns factorial of a passed in number
print("Factorial -> " + str(factorial(12)))
# return the sum of numbers a factorial is made up of
print("Sum of numbers of factorial -> " + str(calc_nums_sum_of_factorial(12)))




    