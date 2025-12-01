# 199: Next Greater Element II (Circular Array)

**Platform:**  LeetCode 503
**Difficulty:**  Medium
**Pattern:**  Monotonic Stack
**Link:** []()

---

## Problem

Find next greater element in circular array.

**Examples:**

```
Input: nums = [1,2,1] 
Output: [2,-1,2]

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
```

---

## Approach

**Intuition:**
- use monotonic stack to loop through the circular array (2* size of array)

**Algorithm:**
1. Declare stack and result array of n=len(array)
2. loop from 2n-1 to 0
    - if stack and stack.top() < current_num: pop the elements
    - append the current_num to the stack

**Complexity:**
- Time: O(N1) + O(N2)
- Space: O(N2)

---

## Solution

```python
class Solution:
    def nextGreaterElement(self, nums: List[int]) -> List[int]:
        n= len(nums)
        result = [-1] * n
        stack = []
        for i in range(2*n-1, -1, -1):
            num = nums[i % n]
            while stack and stack[-1] <= num:
                stack.pop()
            if i < n:
                result[i] = -1 if not stack else stack[-1]
            stack.append(num)
        return result

        
```

---

