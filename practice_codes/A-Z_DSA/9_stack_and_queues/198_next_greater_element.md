# 198. Next Greater Element

**Platform:**  LeetCode 496
**Difficulty:**  Easy
**Pattern:**  Monotonic Stack
**Link:** []()

---

## Problem

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

**Examples:**

```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1] 

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

---

## Approach

**Intuition:**
- use map to store the element and its respective next greater element from list2 and get the greater element for list1 from map

**Algorithm:**
1. Declare hash_map and stack
2. Loop through each element of list2:
    - append the index of each element
    - if stack and top element is < current element, then current element is next greater element for that stack contained elements
3. Again loop through each element of list1:
    - if the map contains the current num, store that values for that index else store -1

**Complexity:**
- Time: O(N1) + O(N2)
- Space: O(N2)

---

## Solution

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        stack = []
        for i in range(len(nums2)):
            while stack and nums[stack[-1]] < nums2[i]:
                hash_map[stack.pop()] = nums2[i]

            stack.append(i)
        
        result = [-1] * len(nums1)
        for i in range(len(nums1)):
            result[i] = hash_map.get(nums1[i], -1)
        return result

        
```

---

