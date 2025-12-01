# 203. Asteroid Collision

**Platform:**  LeetCode 735
**Difficulty:** Medium
**Pattern:**  stack
**Link:** [Click here](https://leetcode.com/problems/asteroid-collision/description/)

---

## Problem

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

**Examples:**

```
Input: asteroids = [5,10,-5]
Output: [5,10]

Input: asteroids = [8,-8]
Output: []

Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
```

---

## Approach

**Algorithm:**

1. **Initialize an empty stack**. This stack stores asteroids that are “alive” so far.

2. **Iterate through each asteroid** in the array.

   **Case A: Positive asteroid (>0)**

   * Append it to the stack.
   * It can only collide with future negative asteroids.

   **Case B: Negative asteroid (<0)**

   * While the stack is **non-empty** and the **top of stack is positive**, a collision occurs:

     * If `abs(asteroid) > stack[-1]`: pop the top (right-moving asteroid destroyed), continue checking the next top.
     * If `abs(asteroid) == stack[-1]`: pop the top (both destroyed), stop processing this asteroid.
     * If `abs(asteroid) < stack[-1]`: the negative asteroid is destroyed, stop processing.
   * If the stack is empty **or the top is negative**, append the current negative asteroid to the stack.

3. After processing all asteroids, the stack contains the **surviving asteroids** in order.

**Complexity:**
- Time: O(N)
- Space: O(N)

---

## Solution

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for i, num in enumerate(asteroids):
            # postive asteroid
            if num > 0:
                result.append(num)

            # negative asteroid
            else:
                while result and result[-1] > 0 and result[-1] < abs(num):
                    result.pop()
                if result and result[-1] == abs(num):
                    result.pop()
                    continue
                if not result or result[-1] < 0:
                    result.append(num)
        return result
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


Here’s a **clean, proper explanation** of the intuition and approach for **Asteroid Collision (LeetCode 735)**.

---

# 🔹 **Intuition**

* Each asteroid moves either **right (positive)** or **left (negative)**.
* Asteroids moving in the **same direction never collide**.
* A collision occurs **only when a right-moving asteroid meets a left-moving asteroid**.

We want to simulate **all collisions efficiently**, keeping only the asteroids that survive.

Key idea:

* Use a **stack** to represent asteroids moving right that haven’t collided yet.
* When a **left-moving asteroid** appears, it may collide with **all right-moving asteroids in the stack**, starting from the top.
* Pop from the stack until either:

  * the left-moving asteroid is destroyed, or
  * all colliding right-moving asteroids are destroyed, in which case the left-moving asteroid survives and is added to the stack.

This allows us to process collisions **in one pass**, **O(n)** time.

---

# 🔹 **Step-by-step Approach**


---

# 🔹 **Key Points / Tricks**

* **Only right vs left collisions matter** (positive vs negative).
* **Stack stores surviving right-moving asteroids** waiting to collide.
* **Negative asteroid may destroy multiple positive asteroids** in a row.
* **Order matters** — stack ensures the correct relative position is preserved.

---
