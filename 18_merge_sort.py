"""
Merge Sort

arr = [5, 7, 8, 4, 1, 6, 9, 2]

Time Complexity = O(n log(n))
Space Complexity = O(n)

"""

def merge_sort(arr):
  if len(arr) == 1:
    return arr
  
  arr1, arr2 = divide_array(arr)

  a1 = merge_sort(arr1)
  a2 = merge_sort(arr2)

  data = merge_arr(a1, a2)
  return data

# Divide Array
def divide_array(arr):
  n = len(arr)

  mid = n // 2

  return arr[:mid], arr[mid:]

# Merge Two Array with sorting
def merge_arr(arr1, arr2):
  i = 0
  j = 0

  result = []

  while i < len(arr1) and j < len(arr2):
    if arr1[i] > arr2[j]:
      result.append(arr2[j])
      j += 1
    else:
      result.append(arr1[i])
      i += 1

  # Remainig elements from arr1
  while i < len(arr1):
    result.append(arr1[i])
    i += 1

  # Remianing elements from arr2
  while j < len(arr2):
    result.append(arr2[j])
    j += 1

  return result


arr =[3,1,2]
data = merge_sort(arr)
print(data)