"""
Bubble Sort

arr = [5, 7, 8, 4, 1, 6, 9, 2]

How To Solve:
Compare Number that is surrounds you and when you found big number then move it to the right side


"""

def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    print(f"______ Phase - {i + 1} ______")
    for j in range(0, n - 1 - i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      print(arr)

arr = [3, 2, 1, 4, 1]
bubble_sort(arr)
# print(arr)