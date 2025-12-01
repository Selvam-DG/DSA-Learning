# 188. Implement Stack Using Queue

**Platform:** LeetCode 225
**Difficulty:** Easy
**Pattern:** Stack / Queue
**Link:** 

---

## Problem

Implement Stack using queue data structure

**Examples:**

```
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]
```

---

## Approach

**Intuition:**
- [Your thought process]

**Algorithm:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Complexity:**
- Time: O(1)
- Space: O(N)

---

## Solution

```python
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()        

    def push(self, x: int) -> None:
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q2.popleft()
        
    
    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return not self.q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

---


## Approach

**Intuition:**
- Use one stack, append and rotate the elements

**Algorithm:**
1. `push` -> append the element to the stack and rotate the element 
2. `pop` -> pop the element from stack
3.  `top` -> top the element from stack
4. `is_empty` -> return true if stack

**Complexity:**
- Time: O(1)
- Space: O(N)

---

## Solution

```py
class MyStack:
    def __init__(self):
        self.queue = deque()
    
    def push(self, x: int):
        self.queue.append(x)
        size = len(self.queue)

        for _ in range(size - 1):
            self.queue.append(self.queue.popleft())
    
    def pop():
        return self.queue.popleft()
    
    def top():
        return self.queue[0]
    
    def empty(self):
        return not self.queue

```