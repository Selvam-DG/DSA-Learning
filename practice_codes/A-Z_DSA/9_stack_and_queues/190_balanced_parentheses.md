# 20. Valid Parentheses

**Platform:** LeetCode  20
**Difficulty:** Easy  
**Pattern:** Stack  
**Link:** https://leetcode.com/problems/valid-parentheses/

---

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

**Examples:**

```
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```

---

## Approach

**Intuition:**
- Use a stack to track opening brackets
- When we see a closing bracket, check if it matches the last opening bracket
- Use a hash map to store bracket pairs for quick lookup

**Algorithm:**
1. Create a map of closing → opening brackets
2. Loop through each character
3. If opening bracket → push to stack
4. If closing bracket → check if it matches top of stack
5. Return true only if stack is empty at the end

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Solution


```py
class Solution:
    def isValidParentheses(self, s: str) -> bool:
        pair_map = {"]": "[", "}": "{", ")": "("}
        stack = []

        for char in s:
            if char in pair_map.values():
                stack.append(char)
            
            elif char in pair_map.keys():
                if stack and stack[-1] == pair_map[char]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
    
    def isVaidParentheses(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            if stack:
                last = stack[-1]
                if self.is_valid(last, s[i]):
                    stack.pop()
                    continue
            stack.append(s[i])
        return not stack
    
    def is_valid(self, last, curr):
        if last == "(" and curr = ")" or last == "[" and curr = "]" or last == "{" and curr = "}":
            return True
        return False

```
