# 200: 1. Next Smaller Element

**Platform:** GeeksforGeeks
**Difficulty:** Easy
**Pattern:** Monotonic Stack
**Link:** []()

---

## Problem

Find next smaller element foreach element in array.

**Examples:**

```
Input: arr[] = [4, 8, 5, 2, 25] 
Output: [2, 5, 2, -1, -1]


```

---

## Approach

**Intuition:**
- Use Monotonic stack to store the indices of elements and when condition satisfies, mark the result for respective index of result

**Algorithm:**

1. Create a result array of size `n` and fill it with `-1`, because some elements may not have any smaller element on their right.
2. Create an empty stack that will store indices of elements.
   This stack will help you track candidates whose next smaller element hasn’t appeared yet.
3. Traverse the array from left to right using index `i`.
4. While the stack is not empty **and** the current element `nums[i]` is smaller than the element at the index on top of the stack:

   * Pop the index from the stack.
   * Assign the current element as the next smaller element for that popped index.
5. After processing, push the current index `i` onto the stack.
6. When the loop ends, any indices still in the stack do not have a next smaller element, so their values remain `-1`.
7. Return the result array.


---

**Complexity:**
- Time: O(N)
- Space: O(N)

---

## Solution

```python
class Solution:
    def nextSmallerElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result

    
    def nextSmallerElement2(self, nums: List[int]) -> List[int]:
        n = len(result)
        nse = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1]  >= nums[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return nse



```

---


# 2. Previous Smaller Element (PSE) 

## Approach

**Goal:** For each element, find the first smaller element to its **left**.

### **Algorithm**

1. Create a result array `pse` of size `n` and fill it with `-1` because some elements may not have any smaller element on their left.
2. Create an empty stack that will store elements (or indices) in increasing order.
3. Traverse the array from left to right using index `i` and element `num = nums[i]`.
4. While the stack is not empty and the top element of the stack is **greater than or equal to** the current element:

   * Pop from the stack because those elements cannot be the previous smaller element.
5. After popping, if the stack is not empty, the top of the stack is the previous smaller element for the current index.
   Otherwise, assign `-1` because no smaller element exists to the left.
6. Push the current element (or index) onto the stack.
7. Continue until the end of the array and return the `pse` array.

---

```python
class Solution:
    
    def previousSmallerElemen(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pse = [-1] * n
        stack = []
        for i,num in enumerate(nums):
            while stack and stack[-1] >= num:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(num)
        return pse

 

```

# 3. Previous Greater Element (PGE) 
## Approach

**Goal:** For each element, find the first greater element to its **left**.

### **Algorithm :**

1. Create a result array `pge` of size `n` and fill it with `-1`.
2. Create an empty stack that stores elements (or indices) in decreasing order.
3. Traverse the array from left to right using index `i` and element `num = nums[i]`.
4. While the stack is not empty and the top element of the stack is **less than or equal to** the current element:

   * Pop from the stack, because those elements cannot be the previous greater element.
5. If the stack is not empty after popping, the top of the stack becomes the previous greater element.
   Otherwise, assign `-1`.
6. Push the current element onto the stack.
7. After finishing the traversal, return the `pge` array.

---

```python
class Solution:

    def previousGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pge = [-1] * n
        stack = []
        for i,num in enumerate(nums):
            while stack and stack[-1] <= num:
                stack.pop()
            pge[i] = stack[-1] if stack else -1

            stack.append(num)

        return pge

```
---