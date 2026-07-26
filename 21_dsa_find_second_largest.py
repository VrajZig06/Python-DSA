# Problem: Find Second largest element from the array without sorting

arr = [10,10, 10]

def second_largest(arr):
  first_largest = float("-inf")
  second_largest =  -1

  for i in range(len(arr)):
    if arr[i] > first_largest:
      if second_largest < first_largest and first_largest != second_largest:
        second_largest = first_largest
        first_largest = arr[i]
      else:
        first_largest = arr[i]

  return second_largest

print(second_largest(arr))
