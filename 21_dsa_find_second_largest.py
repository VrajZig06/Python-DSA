# Problem: Find Second largest element from the array without sorting

arr = [3,4,5,1,2,3,8,9,10]

def second_largest(arr):
  first_largest = float("-inf")
  second_largest = float("-inf")

  for i in range(len(arr)):
    if second_largest < arr[i]:
      if first_largest < second_largest:
        first_largest = second_largest

      second_largest = arr[i]

  return first_largest

print(second_largest(arr))
