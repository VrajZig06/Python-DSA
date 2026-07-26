# Problem: Find Second largest element from the array without sorting

arr =[10, 10, 10]

def second_largest(arr):
  first_largest = float("-inf")
  second_largest = float("-inf")

  for i in range(len(arr)):
    if second_largest < arr[i]:
      if first_largest < second_largest:
        first_largest = second_largest
      else:
        return - 1

      second_largest = arr[i]

  return first_largest

print(second_largest(arr))
