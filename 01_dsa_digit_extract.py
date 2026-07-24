# Problem 1: Extarcting Digits from Number

def extracting_nums(num):
    while num > 0:
        last_digit = num % 10
        print(f"last_digit :: {last_digit}")
        num //= 10

extracting_nums(123)

"""
Time Complexity: O(log 10 num)
space_compexity: O(1)
"""