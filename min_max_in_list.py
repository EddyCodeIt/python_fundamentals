import random

# First, lets generate a list of some specified size with random numbers in range from 0 to 100
def list_of_rand_nums(listSize):
    numList = []
    for num in range(listSize):
        randNum = random.randrange(1, 101, 1)
        numList.append(randNum)
    print(numList)
    return numList

#list_of_rand_nums(10) 

# Define a function that takes in a list with random numbers,
# itterates over it and decides which number is largest and 
# which is smallest, than returns a list with those 2 numbers

def find_min_max(numList):
    tempMin, tempMax, min_max_list = numList[0] , 0 , [] # variables involved

    for num in numList:

        if(num <= tempMin):
            tempMin = num
        else:
            if(num >= tempMax):
                tempMax = num

    min_max_list.append(tempMin)
    min_max_list.append(tempMax)
    
    return min_max_list

print(find_min_max(list_of_rand_nums(10)))



    
