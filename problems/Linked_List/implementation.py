class Node:
    def __init__(self, value= None, next = None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, value):
        node = Node(value, self.head)
        self.head = node
    
    def insert_at_end(self,value):
        if self.head is None:
            node = Node(value, self.head)
            self.head = node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value, None)
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(count)
        return count
    
    def  insert_at_index(self, index, value):
        if index < 0:
            raise Exception('Invalid Index')
        elif index == 0:
            self.insert_at_begining(value)
            return
        elif index > self.length():
            self.insert_at_end(value)
            return
        count = 0
        current = self.head
        while current:
            if count +1  == index:
                node= Node(value, current.next)
                current.next = node
                break
            count += 1
            current = current.next       
    def remove_at_index(self, index):
        if index < 0 and index >= self.length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        current = self.head
        while current:
            if count +1  == index:
                current.next = current.next.next
                break
            count += 1
            current = current.next
    def insert_values(self, data:list):
        if self.head is None:
            for value in data:
                self.insert_at_end(value)
            return
        current = self.head
        while current.next:
            current= current.next
        for value in data:
            current = self.insert_at_end(value)
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception('Cannot insert in Null List ')
        
        if self.head.value = data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        current = self.head
        setter = 0
        while current:
            if current.value == data_after:
                setter +=1
                current.next = Node(data_to_insert, current.next)
                break
            current = current.next
        if setter == 0:
            print("The value not found in Linked List!!!!")
    
    def remove_by_value(self,value):
        if self.head is None:
            raise Exception("Cannot remove value from Empty Linked List")
        elif self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        setter = 0
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                setter += 1
                break
            current = current.next
        if setter == 0:
            print("Value not Found !!!!")
            
        
    
    
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return
            
        current = self.head
        result = ''
        while current:
            result += str(current.value) + ' --> '
            current = current.next
        result += 'None'
        
        print(result)
'''
linked_list = LinkedList()
linked_list.insert_at_end(22)
linked_list.insert_at_begining(5)
linked_list.insert_at_begining(23)
linked_list.print()
linked_list.length()
linked_list.insert_at_end(55)

linked_list.print()

linked_list.insert_at_index(2,333)
linked_list.insert_at_index(100,20)

linked_list.print()
linked_list.length()
linked_list.remove_at_index(3)
linked_list.print()

linked_list.insert_values([22,7,85,44])
linked_list.print()
'''
ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()
