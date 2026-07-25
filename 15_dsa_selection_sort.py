"""
# Selection Sort

arr = [5, 7, 8, 4, 1, 6, 9, 2]

How to Solve:
take first element and assume that number is minimum and then compare with the list of right side and if you find then just replace this things

Time Complexity = O(n^2)
Space Complexity = O(1)
"""

def selection_sort(arr):
  n = len(arr)
  for i in range(n -1):
    min_index = i

    for j in range(i + 1, n):

      if arr[min_index] > arr[j]:
        min_index = j

    # swap min_index with current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [5, 7, 8, 4, 1, 6, 9, 2, 1]
selection_sort(arr)
print(arr)