# Merge Sort

**Merge Sort** is a divide and conquer algorithm. It divides the input array into two halves, sorts each half, and then merges them back together.

### Algorithm

1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the sorted halves.

### Time Complexity

- **Best-case**: O(n log n)
- **Average-case**: O(n log n)
- **Worst-case**: O(n log n)

### Space Complexity
O(n) (requires additional space for the temporary arrays)

### Example

Given the sequence: **7, 2, 1, 6**.

- Split: [7, 2] and [1, 6]
- Sort halves: [2, 7] and [1, 6]
- Merge: [1, 2, 6, 7]

**Final Sorted Array**: **1, 2, 6, 7**
