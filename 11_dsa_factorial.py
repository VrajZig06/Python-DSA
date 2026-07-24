# Problem: Find Factorial of the given number using the recursion

def fac(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fac(n - 1)

# Time Compexity: O(n)
# Space Complexity: O(n) -> Stack Space

print(fac(5))