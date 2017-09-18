# To find Fizz, Buzz and FizzBuzz in range of 0 to 100
# python allows us to loop through this set of numbers
# using for loop construct. For convenience, we can use a 
# function range(n), where n is a number to specify range from
# 0 to n. 
# To decide which number is Fizz, Buzz or FizzBuzz we use if/elif 
# decision tree construct. 
# To solve the actual problem of finding numbers that are multiple of
# either 3, 5 or both, we could evaluate if / elif statements to true if
# current value for i in the loop in modulus with 3, 5, or both has remainder 
# of 0, i.e., 9 % 3 == 0 would evaluate to true. Now we would be able to execute 
# print() function with fizz, buzz and FizzBuzz. 
for i in range(100):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5 == 0:
        if i % 3 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(i)

