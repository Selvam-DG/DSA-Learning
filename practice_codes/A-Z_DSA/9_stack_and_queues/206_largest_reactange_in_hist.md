# 206. Largest Element in Histogram

**Platform:** LeetCode 84
**Difficulty:** Hard
**Pattern:** Monotonic Stack
**Link:** []()

---

## Problem

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

**Examples:**

```
Input: heights = [2,1,5,6,2,3]
Output: 10

Input: 
Output: 
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
- Time: O(?)
- Space: O(?)

---

## Solution

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse = self.previousSmallerElement(heights)
        nse = self.nextSmallerElement(heights)
        result = 0
        for i in range(heights):
            area = height[i] *(nse-pse-1)
            result = max(result, area)
        return result

    def previousSmallerElement(self, heights):
        n = len(heights)
        pse = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        
    def nextSmallerElement(self, heights):
        n = len(heights)
        nse = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            nse[i] = stack[-1] if stack else n
            stack.append(i)

    
```

---

## Key Points

- [Important insight 1]
- [Important insight 2]
- [Important insight 3]

---
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxArea = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                element = stack.pop()
                nse = i
                pse = stack[-1] if stack else -1
                area =( nse-pse-1) * heights[element]
                maxArea = max(area, maxArea)
            stack.append(i)
        
        while stack:
            element = stack.pop()
            nse = n
            pse = stack[-1] if stack else -1
            area = heights[element] * (nse - pse - 1)
            maxArea = max(area, maxArea)
        return maxArea
```