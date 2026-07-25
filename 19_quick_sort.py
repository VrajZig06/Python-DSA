"""
Quick Sort

arr = [5, 7, 8, 4, 1, 6, 9, 2]

Take Pivot and put it with its correct positions

Time Complexity = O(n log n) BEST AND AVERAGE 
Space Complexity = (1)

WORST CASE: 
arr = [5,5,5,5,5,5,5,5,5,5,5,5]
Time Complexity = O(n ^ 2)


"""
def partition(arr, low, high):
  i = low
  j = high
  pivot = arr[low]

  while i < j:
    while i <= high and arr[i] <= pivot:
      i += 1

    while j >= low and arr[j] > pivot:
      j -= 1

    if i < j:
      arr[i], arr[j] = arr[j], arr[i]

  arr[low], arr[j] = arr[j], arr[low]

  return j

def quick_sort(arr, low, high):
  if low < high:
    mid = partition(arr, low, high)
    quick_sort(arr, low, mid - 1)
    quick_sort(arr, mid + 1, high)
   
arr = [5, 7, 8, 4, 1, 6, 9, 2]
quick_sort(arr, 0 , len(arr) - 1)
print(arr)