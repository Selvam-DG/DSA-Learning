

# 191. Min Stack

**Platform:**LeetCode 155  
**Difficulty:** Medium
**Pattern:** Stack Design 
**Link:** [Problem URL]

---

## Problem

Design stack that supports push,pop, top, and retrieving minimum element in constant time.

**Examples:**

```
Input:  ["MinStack","push","push","push","getMin","pop","top","getMin"] [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]

Input: 
Output: 
```

---

## Approach

**Intuition:**
- Use two stacks - one for elements, one for minimum values

**Algorithm:**
0. declare stack and minstack
1. if push the value, append to stack and also append to min stack if value less than the top value of min stack
2. if pop, remove the top value and if top value is the min value in the min stack, remove it
3. if top, return top element in the stack
4. for min value, return the top value in min stack

**Complexity:**
- Time: O(1)
- Space: O(n)

---

## Solution

```py
class MinStack:

    def __init__(self):
        self.__stack = []
        self.__minStack = []
        

    def push(self, val: int) -> None:
        if  not self.__minStack or val <= self.__minStack[-1]:
            self.__minStack.append(val)
        self.__stack.append(val)
        

    def pop(self) -> None:
        value = self.__stack.pop()
        if value == self.__minStack[-1]:
            self.__minStack.pop()
        

    def top(self) -> int:
        return self.__stack[-1]
        

    def getMin(self) -> int:
        return self.__minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

---

## Approach

**Intuition:**
- Use one stack with list of [value, minvalue]

**Algorithm:**
0. declare stack 
1. `push` -> append the element along with the value if stack is empty or else compare the min value with current value and append the min value
2. if pop, remove the top value 
3. if top, return top element in the stack
4. for min value, return the top element first index value

**Complexity:**
- Time: O(1)
- Space: O(n)

---

## Solution

```py
class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            stack.append([val, val])
        else:
            currentMin = Min(val, stack[-1][1])
            stack.append([val, currentMin])
        

    def pop(self) -> None:
        stack.pop()
        
        

    def top(self) -> int:
        return stack[-1][0]
        
        

    def getMin(self) -> int:
        return stack[-1][1]
        
        
```