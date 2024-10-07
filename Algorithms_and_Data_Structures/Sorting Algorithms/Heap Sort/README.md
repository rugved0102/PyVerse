# Heap Sort

**Heap Sort** is a comparison-based sorting algorithm that uses a binary heap data structure. It first builds a max heap from the input array and then repeatedly extracts the maximum element.

### Algorithm

1. Convert the array into a max heap.
2. Remove the root node (maximum) and replace it with the last node.
3. Heapify the remaining elements.
4. Repeat until the heap is empty.

### Time Complexity

- **Best-case**: O(n log n)
- **Average-case**: O(n log n)
- **Worst-case**: O(n log n)

### Example

Given the sequence: **7, 2, 1, 6**.

1. Build max heap: [7, 2, 1, 6]
2. Extract 7 → [6, 2, 1]
3. Repeat until sorted.

**Final Sorted Array**: **1, 2, 6, 7**
