# define 2 lists to merge
list1 = [1, 4, 6]
list2 = [2, 3, 5]

# define a function that takes 2 lists, merges them and returns unsorted list

def merge_lists(list1, list2):
    list3 = [] # create a 3rd list inside function that will take content of two lists from parameters
    for item in list1:
        list3.append(item) # loop list1 and add each item into list3
    for item in list2:
        list3.append(item) # repeat same with list2

    return list3 # return unsorted list

print(merge_lists(list1, list2)) # run function and print returned merged list
