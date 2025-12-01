Implementing Stack Using Array


Problem : Implement Stack Operations Using Arrays. Operations like append(), pop(), top(), isEmpty(), len()
Platform: -
Difficulty: Easy
Pattern:
Input:
Output:
Approach: use Array with top pointer, manage overflow and underflow

```py
class MyStack:
    def __init__(self, capacity):
        self.__top = -1
        self.__capacity = capacity
        self.__arr = [None] * capacity

    def is_empty(self):
	    return self.__top == -1
    
    def is_full(self):
        return self.__top == capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack Overflow: Cannot push, stack is full")
        self.__top += 1
        self.__arr[self.__top] = value

    def pop(self):
        if self.is_empty():
	        raise IndexError("Stack Underflow: Cannot pop, stack is empty")

        element = self.__arr[self.__top]
        self.__arr[self.__top] = None
	    self.__top -= 1
        return element

    def peek(self):
        if self.__top == -1:
            raise IndexError("Stack is empty")
        return self.__arr[self.__top]

    def size(self):
        return self.__top + 1

    def __str__(self):
        if self.is_empty:
            return []
        return self.__arr[:self__top + 1 ]
```
```py     
// Stack Implemenatation using Dyanamic Array
class DynamicStack:
    def __init__(self, initial_capacity=2):
        self.__capacity = initial_capacity
        self.__top = -1
        self.__arr = [None] * initial_capacity

    def push(self, value):
        if self.is_full():
            self.__resize()
        self.__arr[self.__top] = value
        self.__top += 1

    def pop():
        if self.is_empty:
            return IndexError("Stack is empty")
        value = self.__arr[self.__top]
	self.__arr[self.__top] = None
        self.__top -= 1
        return value

    def peek(self):
        if self.is_empty():
            return IndexError("Stack is empty")
        return self.__arr[self.__top]


    def size(self):
        return self.__top + 1

    def is_empty(self):
	    return self.__top == -1

    def is_full(self):
        return self.__top == capacity - 1

    def __resize(self):
        new_capacity = self.__capacity * 2
        self.__capacity = new_capacity
        new_stack = [None] * new_capacity
        for i in range(self.__top + 1):
	    new_stack[i] = self.__arr[i]
        self.__arr = new_stack
    
    def __str__(self):
        if self.is_empty():
	        return []
	    return self.__arr[:self.__top + 1]
```