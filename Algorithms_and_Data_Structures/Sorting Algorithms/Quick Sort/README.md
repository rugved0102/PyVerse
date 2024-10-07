# Quick Sort

**Quick Sort** is a divide and conquer algorithm that picks a pivot and partitions the array around it.

### Algorithm

1. Select a pivot element.
2. Partition the array into elements less than the pivot and elements greater than the pivot.
3. Recursively apply the same process to the sub-arrays.

### Time Complexity

- **Best-case**: O(n log n)
- **Average-case**: O(n log n)
- **Worst-case**: O(n²)

### Example

Given the sequence: **7, 2, 1, 6**.

1. Choose pivot: 6.
2. Partition: [2, 1] and [7].
3. Sort partitions: [1, 2, 6, 7].

**Final Sorted Array**: **1, 2, 6, 7**
