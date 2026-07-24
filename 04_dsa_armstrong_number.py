# Problem: Check Given Number is Armstrong Number

# Function: Find number of digits 
import math
def count_digits(num):
    return int(math.log10(num) + 1)

def check_armstrong_number(num):
    length_digit = count_digits(num)

    sum = 0
    n = num

    while n > 0:
        last_digit = n % 10
        sum += last_digit ** length_digit

        n //= 10
    
    return sum == num

print(f"check_armstrong_number :: {check_armstrong_number(123)}")
