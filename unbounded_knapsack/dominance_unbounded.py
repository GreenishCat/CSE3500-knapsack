# Saanvi Mammai
import time 

def dominant_dp(capacity, items):
    """
    items: list of tuples (weight, value)
    capacity: max weight capacity of knapsack
    """

    #Initialize dominant set with single solution: value=0, weight=0
    dominant_set = [(0, 0)]  # list of (value, weight)

    #Iterate over each item
    for weight, value in items:
        new_solutions = []
        #Generate new solutions by adding this item to each existing solution
        for v, w in dominant_set:
            while w + weight <= capacity:
                v += value
                w += weight
                new_solutions.append((v, w)) # changed order of value and weight
        #Merge old and new solutions
        candidate_solutions = dominant_set + new_solutions
        #Sort candidate solutions by weight
        candidate_solutions.sort(key=lambda x: (x[1], -x[0]))

        #Apply dominance rule to prune dominated solutions
        new_dominant_set = []
        max_value_so_far = -1

        for val, wt in candidate_solutions:
            if val > max_value_so_far:
                new_dominant_set.append((val, wt))
                max_value_so_far = val  # Update the max value

        dominant_set = new_dominant_set  # Update dominant set

    return max(val for val, _ in dominant_set)
