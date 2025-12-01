# Problem 202: Sum of Subarray Minimums

**Platform:** LeetCode 907
**Difficulty:** Medium
**Pattern:** Monotonic Stack
**Link:** []()

---

## Problem

Find sum of minimum element of all subarrays.

**Examples:**

```
Input: arr = [3,1,2,4] 
Output: 17 
Explanation: 
    Subarrays are [3],[1],[2],[4],[3,1],[1,2],[2,4],[3,1,2],[1,2,4],[3,1,2,4] 
    Minimums are 3,1,2,4,1,1,2,1,1,1. 
    Sum = 17.

 
```

---

## Approach - BruteForce

**Intuition:**
- [Your thought process]

**Algorithm:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Complexity:**
- Time: O(N²)
- Space: O(1)

---

## Solution

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            mini = arr[i]
            for j in range(i, n):
                mini = min(mini, arr[j])
                res + = mini
        return res

```

---

## Solution

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0
        nse = self.nextSmallerElement(arr)
        psee = self.previousSmallerEqualElemet(arr)
        total = 0
        mod = 10**9 + 7
        for i, num in enumerate(arr):
            left = i - psee[i]
            right = nse[i] - i
            total = (total + (right * left * num) % mod ) % mod

        return total

    def nextSmallerElement(self, arr):
        nse = [n] * n
        stack = []
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i]  = stack[-1] if stack else n
            stack.append(i)
        return nse
               
        
    def previousSmallerEqualElement(self, arr):
        psee = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            psee[i] = stack[-1] if stack else -1
            stack.append(i)
        return psee


```

---


## Key Points

- [Important insight 1]
- [Important insight 2]
- [Important insight 3]

---

## Related Problems

- [Problem name] ([Difficulty])
- [Problem name] ([Difficulty])