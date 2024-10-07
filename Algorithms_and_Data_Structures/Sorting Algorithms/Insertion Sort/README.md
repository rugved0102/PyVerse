# Insertion Sort

**Insertion Sort** is a sorting algorithm that builds a sorted array one element at a time. It is more efficient for small datasets and generally performs better than Selection Sort or Bubble Sort.

### Algorithm

1. Maintain a sub-array that is always sorted.
2. Take elements from the unsorted part and place them in the correct position in the sorted part.

### Time Complexity

- **Best-case**: O(n)
- **Average-case**: O(n²)
- **Worst-case**: O(n²)

### Space Complexity
O(1) (in-place sorting)

### Example

Given the sequence: **7, 2, 1, 6**.

- (7, 2, 1, 6) → (2, 7, 1, 6) – Compare and insert 2 before 7.
- (2, 7, 1, 6) → (2, 1, 7, 6) – Compare and insert 1 before 7.
- (2, 1, 7, 6) → (1, 2, 7, 6) – Insert 1 before 2.
- (1, 2, 7, 6) → (1, 2, 6, 7) – Finally, insert 6 before 7.

**Final Sorted Array**: **1, 2, 6, 7**
