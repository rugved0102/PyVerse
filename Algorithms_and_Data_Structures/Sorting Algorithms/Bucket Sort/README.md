# Bucket Sort

**Bucket Sort** is a sorting algorithm that distributes elements into several buckets. Each bucket is then sorted individually, often using another sorting algorithm.

### Algorithm

1. Create an array of empty buckets.
2. Distribute elements into the corresponding buckets based on some criteria.
3. Sort each bucket individually.
4. Concatenate all buckets to get the final sorted array.

### Time Complexity

- **Best-case**: O(n + k)
- **Average-case**: O(n + k)
- **Worst-case**: O(n²)

### Space Complexity
O(n + k) (where n is the number of elements and k is the number of buckets)

### Example

Given the sequence: **[0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]**.

1. Create buckets.
2. Distribute elements into buckets.
3. Sort each bucket.
4. Concatenate buckets.

**Final Sorted Array**: **[0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]**
