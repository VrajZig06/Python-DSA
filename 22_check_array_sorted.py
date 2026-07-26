# Problem: Check if Array is sorted 

def check_arr_sorted(arr):
  if len(arr) == 1:
    return True

  if arr[0] > arr[len(arr) - 1]:
    for i in range(len(arr) - 1):
        if not (arr[i] > arr[i + 1]):
          return False
  else:
    for i in range(len(arr) - 1):
      if not (arr[i] < arr[i + 1]):
        return False

  return True

arr = [1, 2, 3]
print(check_arr_sorted(arr))
