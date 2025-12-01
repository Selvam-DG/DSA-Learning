# 201. Trapping Rain Water

**Platform:** LeetCode
**Difficulty:** Hard
**Pattern:** Monotonic Stack
**Link:** [link](https://leetcode.com/problems/trapping-rain-water/)

---

## Problem

[Brief problem description]

**Examples:**

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9

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
    def trap(self, height: List[int]) -> int:
        prefMax=self.prefixMax(heights)
        sufMax = self.suffixMax(height)
        total = 0
        for i in range(n):
            prefmax = prefMax[i]
            sufmax = sufMax[i]
            total += min(prefmax, sufmax)- arr[i]
        return total

    
    def prefixMax(self, nums):
        
        n = len(nums)
        res = [None] * n
        res[0] = nums[0]
        for i in range(1,n):
            res[i] = max(nums[i], res[i-1])
        return res
    
    def suffixMax(self, nums):
        n = len(res)
        res = [None] * n
        res[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            res[i] = max(nums[i], res[i+1])
        return res
        
```

---


# Optimal Solution:
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = 0
        rightMax = 0
        left = 0
        right = n-1
        total = 0

        while left < right:
            if height[l] <= height[r]: 
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    total += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    total += rightMax - height[right]
                right -= 1
        return total
```