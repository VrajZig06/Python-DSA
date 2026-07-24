# Problem :Check that given string is palindrome or not using recursion and loop

def check_palindrome_loop(text):
    left = 0
    right = len(text) - 1

    while left <= right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
    
    return True

# Using recursion
def check_palindrome_recursion(text, left, right):
    if left > right:
        return True
    
    if text[left] != text[right]:
        return False
    
    return check_palindrome_recursion(text, left + 1, right - 1)


print(check_palindrome_recursion("ababa", 0, 4))