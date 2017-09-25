import math
x = 60 # a number to be square rooted
current = 1 # starting a guess of a square root value from 1

# function that returns a value based on a current guess
def z_next(z):
    return z - ((z*z - x) / (2 * z)) # Newton's formula for calculating square root of a number

while current != z_next(current):
    current = z_next(current)

    # this line allows to break from infinite loop
    # if square root value goes to infinity
    if(math.fabs(current - z_next(current))<0.000000001): break

    print(current)


print("\nSquare root of ", x, " is ", current)