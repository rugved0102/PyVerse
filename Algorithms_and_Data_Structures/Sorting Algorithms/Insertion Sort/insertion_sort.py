## Insertion Sort ##

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
print("Sorted array using Insertion Sort: ", insertion_sort(arr))

# Output:
# Sorted array using Insertion Sort: [5, 6, 11, 12, 13]
