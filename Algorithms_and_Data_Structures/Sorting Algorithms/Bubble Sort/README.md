# Bubble Sort

**Bubble Sort** is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

### Algorithm

1. Start at the beginning of the array.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Move to the next element and repeat until the end of the array is reached.
5. Repeat the entire process for the array until no swaps are needed.

### Time Complexity

- **Best-case**: O(n) (when the array is already sorted)
- **Average-case**: O(n²)
- **Worst-case**: O(n²)

### Space Complexity
O(1) (in-place sorting)

### Example

Given the sequence: **[5, 1, 4, 2, 8]**.

- First Pass: [1, 4, 2, 5, 8] → (5 and 1 are swapped)
- Second Pass: [1, 2, 4, 5, 8] → (4 and 2 are swapped)
- The array is now sorted.

**Final Sorted Array**: **[1, 2, 4, 5, 8]**
