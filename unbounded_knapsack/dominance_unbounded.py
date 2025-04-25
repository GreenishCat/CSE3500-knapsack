# Saanvi Mammai
import time 

def dominant_dp(items, capacity):
    """
    items: list of tuples (value, weight)
    capacity: max weight capacity of knapsack
    """
    from time import time
    start_time = time()

    #Initialize dominant set with single solution: value=0, weight=0
    dominant_set = [(0, 0)]  # list of (value, weight)

    #Iterate over each item
    for value, weight in items:
        new_solutions = []
        #Generate new solutions by adding this item to each existing solution
        for v, w in dominant_set:
            while w + weight <= capacity:
                new_solutions.append((v + value, w + weight))
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

    end_time = time()
    print(f"Execution Time: {end_time - start_time:.6f} seconds")

    return dominant_set
