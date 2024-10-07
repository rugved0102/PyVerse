## Bubble Sort ##

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array using Bubble Sort: ", bubble_sort(arr))

# Output:
# Sorted array using Bubble Sort: [11, 12, 22, 25, 34, 64, 90]