# Problem: Print 1 to N using recursion


# 1 to N using Head Recursion
def print_number(i, n):
    if i > n:
        return
    
    print(i)
    print_number(i + 1, n)

# print_number(1,5)

# 1 to N using Tail Recursion
def print_tail_recursion(i, n):
    if i <= 0:
        return

    print_tail_recursion(i - 1, n)
    print(i)

# print_tail_recursion(5,5)

# N to 1 using head recursion
def print_head_recursion(n):
    if n == 0:
        return
    
    print(n)
    print_head_recursion(n - 1)

print_head_recursion(5)