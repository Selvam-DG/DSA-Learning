# 192. Infix to Postfix Conversion

**Platform:** GeeksforGeeks
**Difficulty:** Medium
**Pattern:** Stack 
**Link:** []()

---

## Problem

[Brief problem description]

**Examples:**

```
Input: "a+b*(cd-e)(f+gh)-i"
 Output: "abcd^e-fgh+^*+i-"


```

---

## Approach

**Intuition:**
- Use stack for operands and operators and follow the operator precedence rules.

**Algorithm: **

1. Initialize an empty **stack** and an empty **result string**.
2. For each character `ch` in the input expression:

   * If `ch` is an **operand**, append it to `result`.
   * Else if `ch` is an **opening parenthesis `(`**, push it onto the stack.
   * Else if `ch` is an **operator**:

     * While the stack is not empty **and** the top of the stack has **greater or equal precedence**,
       pop it and append it to `result`.
     * Push the current operator `ch` onto the stack.
   * Else if `ch` is a **closing parenthesis `)`**:

     * While the top of the stack is **not `(`**, pop from the stack and append to `result`.
     * Pop the `(` from the stack (but **do not append** it).
3. **After the loop ends:**

   * While the stack is not empty:
     Pop from the stack and append to `result`.

---

If you want, I can also provide a clean Python, Java, or C++ implementation.


**Complexity:**
- Time: O(N)
- Space: O(N)

---

## Solution

```python
class Solution:
    def infixToPostfix(self, s: str) -> str:
        result = "
        stack = []

        for char in s:
            # Operands (isalnum)
            if char.isalnum():
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != '(':
                    result.append(stack.pop())

                stack.pop() # remove the open parentheses
            # Operator
            else:
                while stack and self.precedence(char) <= self.precedence(stack[-1]):
                    result.append(stack.pop())
                stack.push(char)
        
        while stack:
            result.append(stack.pop())
        
        return result

    def precedence(self, char):
        if char in '+-':
            return 1
        elif char in '*/':
            return 2
        elif char in '^':
            return 3
        else:
            return -1


            

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