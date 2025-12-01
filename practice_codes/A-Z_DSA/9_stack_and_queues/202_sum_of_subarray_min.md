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

## Key Points

- [Important insight 1]
- [Important insight 2]
- [Important insight 3]

---

## Related Problems

- [Problem name] ([Difficulty])
- [Problem name] ([Difficulty])