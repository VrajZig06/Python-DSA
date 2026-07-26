# Problem: Remove duplicates array from the sorted array

arr = [1,2,3,4,4,4,5,5,5,5,5,123]

def remove_duplicates(arr):
  map_dict = {}

  for i in range(len(arr)):
    map_dict[arr[i]] = 0

  k = 0
  for j in map_dict.keys():
    arr[k] = j
    k += 1

  return arr[:k]

def optimal_sol(arr):
  i = 0
  j = i + 1

  while j < len(arr):
    if arr[i] != arr[j]:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
    
    j += 1

  return arr[:i + 1]

    


print(optimal_sol(arr))