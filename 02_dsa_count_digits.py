# Problem: Counts Digits from Number
import math

def count_digit(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1

    return count

def count_digit_with_log(num):
    return int(math.log10(num) + 1)

print(f"count_digit :: {count_digit_with_log(123)}")

# Time Complexity : O(log 10 (num))