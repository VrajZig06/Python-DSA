# Problem: Largest Element from the array

arr = [4,5,1,2,8]

def find_largest_element(arr):
  max_value = float("-inf")

  for i in range(len(arr)):
    if arr[i] > max_value:
      max_value = arr[i]


  return max_value

print(find_largest_element(arr))