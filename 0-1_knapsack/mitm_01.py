# Erica Davies

import math

def gen_subsets(superset):
    '''Generates all possible subsets of a given set using binary masking'''
    subsets = []
    n=len(superset)
    for i in range(0,(pow(2,n))): # forumla for number of subsets of a set
        weight_sum = 0
        value_sum = 0
        for j in range(n): # uses binary to determine which element of the subset to in/exclude
            # EX: binary rep of 5 = 101 -> so, for a subset with 3 elements, we include the 1st and 3rd element and exclude the 2nd
            #     if bit is 1, include the element, if bit is 0, exclude the element
            #     this ensures that we get every possible subset for the set given
            bit = (i>>j)&1
            if bit == 1:
                element = superset[j]
                weight_sum += element[0]
                value_sum += element[1]
        subsets.append((weight_sum, value_sum))
    return subsets

def B_subset_filter(subsetB):
    '''Filters the subsets of B to only contain Pareto efficient subsets'''
    subsetB.sort(key = lambda pair: pair[0]) # sort by weight

    filteredB = []
    max_val = -math.inf
    for ele in subsetB:
        if ele[1] > max_val: # if the value is higher than the max seen value, then we keep the element
            max_val = ele[1]
            filteredB.append(ele)
    return filteredB # only returns the tuples with the highest value for their weight

def binary_search_B(filteredB, W):
    '''Standard binary search'''
    low = 0
    high = len(filteredB) - 1
    best_val = -math.inf
    
    while low<=high:
        mid = (low+high)//2
        if filteredB[mid][0] <= W:
            best_val = filteredB[mid][1]
            low = mid+1
        else:
            high = mid-1
    return best_val


def match_AB(subsetA, filteredB, weight):
    '''Finds the most compatible subset in B, ∀ a ∈ A, s.t.
       the value is maximized and the weight is less than or equal to the max weight'''
    max_val = -math.inf
    for ele in subsetA:
        W_remaining = weight - ele[0]
        val_B = binary_search_B(filteredB, W_remaining)
        total_val = ele[1] + val_B
        max_val = max(max_val, total_val)
    return max_val
        

# the following uses an example weight and list of items
weight = 15
items = [(1,2),(3,4),(1,1),(2,3),(4,1)] # tuples in (weight, value)
n = len(items)
A = items[0:n//2] # takes first half of list
B = items[n//2:n] # takes second half of list
subsetA = gen_subsets(A)
subsetB = gen_subsets(B)
filteredB = B_subset_filter(subsetB)
max_value = match_AB(subsetA, filteredB, weight)
print(max_value)
