#  Heap, Heap Sort, Heapify & Priority Queues

A **heap** is a special tree-based data structure that satisfies the **heap property**. It is often used in **priority queues**, **heap sort**, and **graph algorithms** (like Dijkstra).

---

## Binary Tree Basics

### Array Representation of Binary Trees
- A **Full binary tree** is a binary tree where all nodes are filled . Maximum number of nodes in a full binary tree is 2^(h+1) -1

- A **complete binary tree** can be stored in an array without any gaps.
- A **complete binary tree** is a full binary tree upto h-1 (where h-height of binary tree) and the last level fill, the elements are filled from left to right
- If the **root is at index 0**, then:
  - Left child → `2i + 1`
  - Right child → `2i + 2`
  - Parent → `(i - 1) // 2`

---

## Complete Binary Tree

- All levels are completely filled except possibly the last level.
- Nodes are filled from **left to right**.
- This structure is ideal for **heap** implementation using arrays.

---

##  Heap Overview
- A heap is a complete binary tree
### Types of Heaps

| Type       | Property                                |
|------------|------------------------------------------|
| Max Heap   | Every parent node ≥ child nodes          |
| Min Heap   | Every parent node ≤ child nodes          |

---

## Heap Operations

### Insert into Heap (Max Heap)

1. Add element at the end of the array (maintains complete tree).
2. Bubble it up (swap with parent) to maintain heap property.

```python
def insert(heap, val):
    heap.append(val)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] > heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break
```

### Delete from Heap (Max Heap)
1. Replace root with the last element.
2. Remove the last element.
3. Heapify from the root down.
```python
def delete_max(heap):
    if len(heap) == 0:
        return None
    max_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heapify(heap, 0)
    return max_val
```
### Heapify Operation
Ensures the heap property from top to bottom.
```python
def heapify(heap, i):
    size = len(heap)
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < size and heap[left] > heap[largest]:
        largest = left
    if right < size and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        heapify(heap, largest)

```
### Build Heap
Convert an unsorted array into a heap (max/min):
```python
def build_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, i)
```

## Heap Sort
Build a max heap.

Swap root with the last item, reduce heap size, and heapify again.
```python
def heap_sort(arr):
    n = len(arr)
    build_heap(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

def heapify(arr, i, n):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)
```
## Priority Queue Using Heap

A priority queue is a data structure where each element has a priority. The element with highest (or lowest) priority is served first.
- A **max heap** is used for highest priority.
- A **min heap** is used for lowest priority.

### Example using heapq (min heap by default):
```python
import heapq

pq = []
heapq.heappush(pq, 10)
heapq.heappush(pq, 5)
heapq.heappush(pq, 20)

print(heapq.heappop(pq))  # Output: 5 (min priority)
```
To use as a max heap, insert `-value`.
```python
heapq.heappush(pq, -10)
heapq.heappop(pq) * -1  # Output: 10
```
##  Time Complexity Summary
| Operation     | Time Complexity |
| ------------- | --------------- |
| Insert        | O(log n)        |
| Delete (Root) | O(log n)        |
| Heapify       | O(log n)        |
| Build Heap    | O(n)            |
| Heap Sort     | O(n log n)      |

<img width="1024" height="1536" alt="6fa43ae4-d372-4a69-b6da-ac2b106b9740" src="https://github.com/user-attachments/assets/2144f551-2386-481c-9c5b-c299fe5c2a3a" />

## References
[Abdul Bari – Heap, Heapify, Heap Sort, Priority Queue (YouTube)](https://www.youtube.com/watch?v=HqPJF2L5h9U&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=32&ab_channel=AbdulBari)
