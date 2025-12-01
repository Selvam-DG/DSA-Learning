# 189. Implement Queue Using Stack

**Platform:** LeetCode 232
**Difficulty:** Easy
**Pattern:** Stack / Queue
**Link:** [link](https://leetcode.com/problems/implement-queue-using-stacks/description/)

---

## Problem

Implement Queue using Stack data structure

**Examples:**

```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
```

---

## Approach

**Intuition:**
- Use two stack, one for push and one for pop

**Algorithm:**
1. `push` -> append the element to the stack1
2. `pop` -> pop the element from stack2. if stack2 is empty, pop the elements from stack1 and append to stack2
3.  `top` -> top the element from stack2. if stack2 is empty, pop the elements from stack1 and append to stack2
4. `is_empty` -> return true if stack1 and stack2 is empty

**Complexity:**
- Time: O(1)
- Space: O(n)

---

## Solution

```python
class MyStack:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.__reshift()
        value = self.stack_out.pop()
        return value        
    
    def peek(self) -> int:
        self.__reshift()
        return self.stack_out[-1]


    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def __reshift(self):
        if not self.stack_out:      # if stack_out is empty
            while self.stack_in:        # loop till stack_in elements
                self.stack_out.append(self.stack_in.pop())  # append the stack_in pop elements to stack_out

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

---

