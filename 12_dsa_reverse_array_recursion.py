# Problem: Reverse the array using the recursion

def reverse_array_recursion(arr, i, j):
    if i > j:
        return 
    
    arr[i], arr[j] = arr[j], arr[i]
    reverse_array_recursion(arr, i + 1, j - 1)

arr = [1,2,3,4,5,7,8]
reverse_array_recursion(arr, 0, len(arr) - 1)
print(arr)
