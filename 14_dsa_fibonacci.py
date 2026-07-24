# Problem: Find the Fibonacci for the given range
# 0, 1, 1, 2, 3, 5, 8
# 0  1  2  3  4  5  6

# Using recursion
def fib_recur(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib_recur(n - 1) + fib_recur(n - 2)

print(f'fib_recur :: {fib_recur(6)}')


# Note: fib(3) = fib(2) + fib(1) = fib(1) + fib(0) + fib(1) = 1 + 0 + 1 = 2