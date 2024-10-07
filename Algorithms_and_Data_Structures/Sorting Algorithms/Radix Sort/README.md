# Radix Sort

**Radix Sort** is a non-comparative sorting algorithm that sorts numbers digit by digit starting from the least significant digit to the most significant digit.

### Algorithm

1. Perform counting sort on each digit.
2. Repeat for all digits.

### Time Complexity

- **Best-case**: O(nk)
- **Average-case**: O(nk)
- **Worst-case**: O(nk)

Here, **n** is the number of elements and **k** is the number of digits in the maximum number.

### Example

Given the sequence: **170, 45, 75, 90, 802, 24, 2, 66**.

1. Sort by least significant digit: **170, 90, 802, 2, 24, 45, 75, 66**.
2. Sort by next significant digit: **2, 24, 45, 66, 75, 90, 170, 802**.

**Final Sorted Array**: **2, 24, 45, 66, 75, 90, 170, 802**
