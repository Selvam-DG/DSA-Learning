# Quick Sort Algorithm

1. Quick Sort Algorithm  
2. Quick Sort Analysis

---

## What is Quick Sort?

**Quick Sort** is a **Divide and Conquer** sorting algorithm.  
It works by:
1. Choosing a **pivot**.
2. Partitioning the array so that:
   - Elements smaller than pivot go to the left.
   - Elements larger than pivot go to the right.
3. Recursively sorting the left and right parts.

---

## Quick Sort Algorithm – Recursive

```python
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # or choose high or middle for better performance
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j
```

## Key Concepts
- Pivot Selection: Can affect performance.
  - First element (basic)
  - Last element
  - Random
  - Median-of-three
- In-place: Requires no extra memory (unlike merge sort).
- Unstable: Doesn't preserve the order of equal elements.

## Time & Space Complexity
| Case    | Time Complexity                |
| ------- | ------------------------------ |
| Best    | O(n log n)                     |
| Average | O(n log n)                     |
| Worst   | O(n²) *(unbalanced partition)* |

## Dry Run Example
Array: `[10, 7, 8, 9, 1, 5]`
1. Pivot = 10
   Partitioned → `[5, 7, 8, 9, 1]` | `10`
2. Recursive call on left:
   Pivot = 5
  Partitioned → `[1]` | `5` | `[7, 8, 9]`
3. Sort recursively...

---
## Example 2:

![quick-sort-450](https://github.com/user-attachments/assets/142b8ba9-d4de-46ee-b504-6c11c981c5cb)

![quicksort-600-1](https://github.com/user-attachments/assets/d2da1aca-e76c-4a9f-939c-6859eb36af02)
---
## Tail Call Optimization (TCO)

To reduce stack depth:
- Always recurse on the smaller part.
- Use loop for the larger part (can make quicksort more space-efficient).


## Quick Sort vs Merge Sort
| Feature         | Quick Sort | Merge Sort |
| --------------- | ---------- | ---------- |
| Time (Avg)      | O(n log n) | O(n log n) |
| Time (Worst)    | O(n²)      | O(n log n) |
| Space           | O(log n)   | O(n)       |
| Stable          |  No       | Yes      |
| In-place        |  Yes      |  No       |
| Practical Speed |  Faster   |  Slower   |

## Partition Techniques
Lomuto Partition Scheme
- Simpler to implement, less efficient in practice.
```python
def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```
## Hoare’s Partition Scheme (used in main example)
- More efficient, fewer swaps.
- Can work better when input has many duplicate values.

## References
Abdul Bari – [Quick Sort Algorithm](https://www.youtube.com/watch?v=7h1s2SojIRw&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=36&ab_channel=AbdulBari)
