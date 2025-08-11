# Dijkstra's Algorithm – Greedy Method


## 1. Introduction

**Dijkstra's Algorithm** is a **greedy** algorithm for finding the **shortest path** from a single source to all other vertices in a **weighted graph** with **non-negative edge weights**.

---

## 2. Problem Definition

Given:
- A weighted, connected graph \( G = (V, E) \)
- A source vertex \( s \)
- Edge weights \( w(u, v) \ge 0 \)

Find:
- The minimum cost (distance) from \( s \) to each vertex \( v \in V \)

---

## 3. Key Features

- Works only for **non-negative weights**.
- Produces shortest paths tree.
- Can use **array** or **priority queue** for efficiency.
- Time complexity depends on data structure choice.

---

## 4. Algorithm Steps

1. **Initialization**:
   - Distance to source = 0
   - Distance to all others = ∞
2. **Repeat** until all vertices are processed:
   - Pick the unvisited vertex with the smallest distance.
   - Update distances to its adjacent vertices if:
     \[
     \text{current distance} + w(u,v) < \text{known distance to v}
     \]
3. Mark vertex as visited.

---

## 5. Time Complexity

| Data Structure         | Time Complexity |
|------------------------|-----------------|
| Adjacency matrix + array | \(O(V^2)\)     |
| Adjacency list + min-heap | \(O(E \log V)\) |

---

## 6. Python Implementation

```python
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, vertex)

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []
}

print(dijkstra(graph, 'A'))
```
---
### 7. Example Walkthrough
```
    A ---4--- B
    | \       |
    2  5      10
    |   \     |
    C ---3--- E ---4--- D ---11--- F
```
- Start at A, distances: A=0, others=∞
- Choose smallest distance vertex → update neighbors
- Continue until all visited

**Final shortest distances from A:**
```
A: 0
B: 4
C: 2
E: 5
D: 9
F: 20
```

## 8. Applications
- GPS navigation systems
- Network routing protocols (OSPF, IS-IS)
- Game AI (pathfinding)
- Traffic flow optimization

## References
Abdul Bari – [Dijkstra's Algorithm](https://www.youtube.com/watch?v=XB4MIexjvY0&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=45&ab_channel=AbdulBari)
