# Merge Sort Algorithm

1. Two-Way Merge Sort – Iterative Method  
2. Merge Sort Algorithm – Recursive  
3. Merge Sort – In-Depth Analysis

---

## Merge Algorithm (Two Sorted Arrays)

This algorithm merges two sorted arrays `A[1..m]` and `B[1..n]` into a new sorted array `C[1..m+n]`.

### Pseudocode

```text
Algorithm Merge(A, B, m, n)
{
    i ← 1; j ← 1; k ← 1
    while (i ≤ m and j ≤ n)
    {
        if A[i] < B[j]
            C[k] ← A[i]; i ← i + 1
        else
            C[k] ← B[j]; j ← j + 1
        k ← k + 1
    }

    for (; i ≤ m; i++)
        C[k] ← A[i]; k ← k + 1

    for (; j ≤ n; j++)
        C[k] ← B[j]; k ← k + 1
}
```

##  Concept Overview

**Merge Sort** is a **Divide and Conquer** algorithm that:
1. **Divides** the array into halves recursively.
2. **Sorts** each half.
3. **Merges** the sorted halves.

It’s known for its **stable sorting**, predictable performance, and **O(n log n)** time complexity in all cases.

---

## Properties

| Property        | Value           |
|----------------|------------------|
| Type           | Comparison-based |
| Stability      | Yes              |
| Time Complexity| O(n log n)       |
| Space Complexity | O(n) (not in-place) |
| Algorithm Type | Divide and Conquer |

---

## Recursive Merge Sort – Algorithm

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Merge step
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```
##  Iterative Merge Sort (Two-Way Merge)

Iteratively merge subarrays of size 1, 2, 4, 8...
```python
def merge_sort_iterative(arr):
    n = len(arr)
    current_size = 1

    while current_size < n:
        for left_start in range(0, n, 2 * current_size):
            mid = min(n - 1, left_start + current_size - 1)
            right_end = min(n - 1, left_start + 2 * current_size - 1)

            merge(arr, left_start, mid, right_end)
        current_size *= 2

def merge(arr, l, m, r):
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

```
### Dry Run Example
Input: [8, 4, 5, 2, 9, 1]

Recursive Breakdown:
```css
[8, 4, 5, 2, 9, 1]
→ [8, 4, 5] and [2, 9, 1]
→ [8], [4, 5] and [2], [9, 1]
→ [4], [5] and [9], [1]
→ Merge and build back up

```
---
![merge-sort-450](https://github.com/user-attachments/assets/1f8022df-e2e9-4d41-b058-0f135282ac89)

---
## Time & Space Complexity
| Case    | Time Complexity |
| ------- | --------------- |
| Best    | O(n log n)      |
| Average | O(n log n)      |
| Worst   | O(n log n)      |
---
## In-depth Analysis Points
- Recursion depth: `log₂(n)`
- Work per level: `O(n)` merges
- Total cost: `O(n log n)`
- Non-adaptive: Always `n log n` even if array is partially sorted
- Cache-unfriendly due to non-local memory access

## Merge Sort vs Other Algorithms 
| Algorithm   | Time       | Space    | Stable | In-place |
| ----------- | ---------- | -------- | ------ | -------- |
| Merge Sort  | O(n log n) | O(n)     | Yes    | No       |
| Quick Sort  | O(n log n) | O(log n) | No     | Yes      |
| Bubble Sort | O(n²)      | O(1)     | Yes    | Yes      |

##  References
Abdul Bari -  [Merge Sort Iterative Method](https://www.youtube.com/watch?v=mB5HXBb_HY8&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=34&ab_channel=AbdulBari)
