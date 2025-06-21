class Node:
    def __init__(self, val= None, next = None):
        self.val = val
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, val):
        node = Node(val, self.head)
        self.head = node
        
    def insert_at_end(self,val):
        if self.head is None:
            self.head = Node(val, None)
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val, None)
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 1
        current = self.head
        while current:
            if count == index-1:
                current.next = current.next.next
                break
            current = current.next
            count += 1
    
    def insert_at(self, index, val):
        if index == 0:
            self.insert_at_begining(val)
        
        elif index < 0:
            raise Exception("Invalid Index")
        
        elif index > self.length():
            self.insert_at_end(val)
        
        curr = self.head
        count = 0
        while curr:
            if count == index-1:
                node = Node(val, curr.next)
                curr.next = node
            count += 1
            curr = curr.next

    def insert_value(self, data):
        if self.head is None:
            self.head = None
            for value in data:
                self.insert_at_end(value)
        for val in data:
            self.insert_at_end(val)
        
        
    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        curr = self.head
        string = ''
        while curr:
            string += str(curr.val) +' --> ' 
            curr = curr.next
        string += ' None'
        print(string)

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_begining(29)
    linked_list.insert_at_begining(55)
    linked_list.insert_at_end(22)
    linked_list.insert_at_end(76)
    linked_list.insert_value([2, 97, 45])
    linked_list.print()
    linked_list.remove_at(4)
    linked_list.insert_at(0, 3)
    linked_list.insert_at(4, 55)
    linked_list.print()
                
    