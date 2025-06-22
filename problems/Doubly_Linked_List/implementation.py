class Node:
    def __init__(self, value=None, prev=None, next = None):
        self.value = value
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_values(self, data:list):
        if self.head is None:
            for value in data:
                self.insert_at_end(value)
            return
        current= self.head
        while current:
            current = current.next
        for value in data:
            self.insert_at_end(value)
        
    def insert_at_begining(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = Node(value, next = self.head)
        self.head.prev = node
        self.head = node
        
    
    def insert_at_end(self,value):
        if self.head is None:
            self.head = Node(value=value)
            return
        
        current = self.head
        while current.next:
            current= current.next        
            
        current.next = Node(value, prev=current)
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(count)
        return count
    def insert_at_index(self, index, value):
        if index < 0:
            raise Exception ("Invalid Index")
        
        if index > self.length():
            self.insert_at_end(value)
            return
        
        if index == 0:
            self.insert_at_begining(value)
            return
        
        current = self.head
        count = 0
        while current:
            if index == count +1:
                current.next = Node(value, prev = current, next = current.next)
                break
            count += 1
            current = current.next
        
        
    def print_forward(self):
        if self.head is None:
            print("Linked List is Empty")
        
        current = self.head
        result = str(self.head.prev) + ' <--> '
        
        while current:
            result += str(current.value) + ' <--> '
            current = current.next
        result += 'None'
        print(result)
        
    def print_backward(self):
        if self.head is None:
            print('Linked List is empty!!!')
        current= self.head
        while current.next:
            current=current.next
        res = str('None') + ' <--> '
        while current:
            res += str(current.value) + ' <--> '
            current =current.prev
        res += 'None'
        print(res)
        
        
if __name__ == '__main__':
    double_linked_list = DoublyLinkedList()
    # double_linked_list.insert_at_begining(2)
    # double_linked_list.insert_at_begining(66)
    # double_linked_list.insert_at_begining(5)
    # double_linked_list.insert_at_begining(219)
    # double_linked_list.insert_at_begining(613)
    # double_linked_list.length()
    
    # double_linked_list.insert_at_end(65)
    # double_linked_list.insert_at_end(35)
    # double_linked_list.insert_at_end(29)
    # double_linked_list.insert_at_end(38)
    # double_linked_list.insert_at_end(255)
    # double_linked_list.print_forward()
    # double_linked_list.print_backward()
    
    double_linked_list.insert_values([1,33,53,6454,765])
    double_linked_list.print_forward()
    double_linked_list.print_backward()
    
    double_linked_list.insert_at_index(2, 5563)
    double_linked_list.print_forward()
    
    