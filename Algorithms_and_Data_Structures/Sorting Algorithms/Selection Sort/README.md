# Selection Sort

**Selection Sort** is a sorting technique that repeatedly finds the minimum element from the unsorted part of the array and puts it at the beginning. It maintains two subarrays: one that is already sorted and one that is unsorted.

### Algorithm

1. Divide the array into a sorted and an unsorted part.
2. Repeatedly select the minimum element from the unsorted part and move it to the sorted part.

### Time Complexity

- **Best-case**: O(n²)
- **Average-case**: O(n²)
- **Worst-case**: O(n²)

### Space Complexity
O(1) (in-place sorting)

### Example

Given the sequence: **7, 2, 1, 6**.

- (7, 2, 1, 6) → (1, 7, 2, 6) – Find the minimum (1) and place it at the start.
- (1, 7, 2, 6) → (1, 2, 7, 6) – Find the next minimum (2) and place it in the second position.
- (1, 2, 7, 6) → (1, 2, 6, 7) – Finally, find the next minimum (6) and place it in the third position.

**Final Sorted Array**: **1, 2, 6, 7**
