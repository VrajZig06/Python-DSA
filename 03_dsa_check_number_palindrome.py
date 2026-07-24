# Problem: Check Number is Palindrome or not

def check_number_palindrome(num):
    n = num
    reverse_num = 0
    while n > 0:
        last_digit = n % 10
        reverse_num = reverse_num * 10 + last_digit

        n //= 10
    
    return reverse_num

print(f"check_number_palindrome :: {check_number_palindrome(123)}")

# Time Complexity = O(log 10 (num))
# Space Complexity = O(k + 1)