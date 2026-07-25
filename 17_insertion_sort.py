"""
Insertion Sort

arr = [5, 7, 8, 4, 1, 6, 9, 2]
"""

def insertion_sort(arr):
  for i in range(1, len(arr)):

    j = i - 1

    temp = arr[i]
    while j >= 0 and temp < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = temp

arr = [5, 7, 8, 4, 1, 6, 9, 2]
insertion_sort(arr)
print(arr)

