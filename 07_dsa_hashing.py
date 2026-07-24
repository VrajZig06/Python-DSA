"""
Problem: Hashing in python

list1 = [5,2,1,2,2,1,7,8,7,5,5,3]
list2 = [10, 111, 115, 11, 9, 8]

-> Constraints
-> 1 <= n[i] <= 10
-> list1 can have 10 ^ 8 elements
-> list2 can have 10 ^ 8 elements

"""

list1 = [5,2,1,2,2,1,7,8,7,5,5,3]
list2 = [10, 111, 115, 2, 11, 9, 8, ]

def brute_force_approach(list1, list2):
    # TC -> O(n) * [O(m) * O(1) * O(1) * O(1)] = O(nm)

    result = {}

    for num in list2: # O(n)
        count = 0
        for inner_numb in list1: # O(m)
            if inner_numb == num: # O(1)
                count += 1 # O(1)

        # Add to dict
        result[num] = count # Average Case : O(1)

    return result

# Function: Create Hashing Dict
def hashing_dict(arr):
    # Time Complexity = O(n)
    hashing_dict = {}

    for i in range(len(arr)):
        hashing_dict[arr[i]] = hashing_dict.get(arr[i], 0) + 1

    return hashing_dict

def optimal_using_hashing(list1, list2):
    # we will use dict data structure to achieve this

    # pre-storing values
    data = hashing_dict(list1) # O(n)
    result = {}

    for i in range(len(list2)): # -> O(m)
        result[list2[i]] = data.get(list2[i], 1) # O(1)
    
    return result

    # Total Time Complexity = O(n) + [O(m) + O(1)] -> O(n+m)

print(f"optimal_using_hashing :: {optimal_using_hashing(list1,list2)}")
