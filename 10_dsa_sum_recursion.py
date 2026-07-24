# Problem: Sum 1 to N using Recursion

# Head Recursion
def sum_nums(i, n, sum):
    if i > n:
        print(f"Sum :: {sum}")
        return
    
    sum += i
    sum_nums(i + 1, n, sum)


sum_nums(1, 5, 0)

# Functional Sum
def functonal_sum(n):
    if n == 1:
        return 1

    return n + functonal_sum(n - 1)

functonal_sum(5)