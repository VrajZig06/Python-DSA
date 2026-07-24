# Problem: Find All Factors of number

import math
def brute_force_approach(num):
    # Time Complexity = O(n)
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors

def average_approach(num):
    # Time Complexity = O(n / 2) ~ O(n + 1) ~ O(n)
    factors = []

    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            factors.append(i)

    factors.append(num)
    return factors

# Optimal solution
def optimal_solution(num):
    # Time Complexity = O(sqrt(n)) + O(1) + O(1) + O(1) + O(1) = O(sqrt(n))
    factors = []

    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)

            if num // i != i:
                factors.append(num // i)

    return factors

print(f"average_approach :: {optimal_solution(36)}")
