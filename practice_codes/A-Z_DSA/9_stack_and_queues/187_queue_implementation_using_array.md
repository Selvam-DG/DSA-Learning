Implementing Queue Using Array


Problem : Implement Queue Operations Using Arrays. Operations like enqueue(), dequeue(), front(), isEmpty(), size()
Platform: -
Difficulty: Easy
Pattern:
Input:
Output:
Approach: use Array with front and rear pointer

```py


class MyQueue:
    def __int__(self, capacity):
        self.__front = 0
        self.__rear = -1
        self.__capacity = capacity
        self.__arr = [None] * capacity
        self.__size = 0
    
    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue Overflow")
        self.__rear += (self.__rear + 1) % self.__capacity
        self.__arr[self.__rear] = value
        self.__size += 1
    
    def dequeue(self):
        if self.is_empty():
            return IndexError("Queue underflow")
        value = self.__arr[self.__front]
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        return value
    
    def front(self):
        if self.is_empty():
            return IndexError("Queue is Empty")
        return self.__arr[self.__front]
    
    def is_empty(self):
        return self.__size == 0
    
    def is_full(self):
        return self.__size == self.__capacity
    
    def size(self):
        return self.__size
    
    def __str__(self):
        if self.is_empty():
            return []
        result = []
        index = self.__front
        for _ in range(self.__size):
            result.append(self.__arr[index])
            index = (index + 1) % self.__capacity
        return str(result)


```

DynamicArray Implementation of Queue
```py

class DynamicStack:
    def __init(self, capacity=2):
        self.__front = 0
        self.__rear = -1
        self.__capacity = capacity
        self.__arr = [None] * capacity
        self.__size = 0
    
    def __resize(self):
        new_capacity = self.__capacity * 2
        new_arr = [None] * new_capacity
        for i in range(self.__size):
            new_arr[i] = self.__arr[(self.__front + i) % self.__capacity ]
        
        self.__arr = new_arr
        self.__capacity = new_capacity
        self.__front = 0
        self.__rear = self.__size - 1
    
    def enqueue(self, value):
        if self.is_full():
            self.__resize()
        self.rear = (self.__rear + 1) % self.__capacity
        self.__arr[self.__rear] = value
        self.__size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.__arr[self.__front]
        self.__arr[self.__front] = None
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        return value
    
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__arr[self.__front]

    def is_empty(self):
        return self.__size == 0
    
    def is_full(self):
        return self.__size == self.__capacity
    
    def size(self):
        return self.__size
    
    def __str__(self):
        if self.is_empty():
            return "Queue([])
        elements = []
        for i in range(self.__size):
            elements.append(self.__arr[self.__front + i] % self.__capacity)
        return "Queue(["+", ".join(elements) + "])"


```