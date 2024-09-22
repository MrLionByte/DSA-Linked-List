
class Node:
    # To initiate the node for linkedList
    def __init__(self,data):
        self.data = data    
        self.next = None
        

class linkedList:
    def __init__(self):
        self.head = None
        
    # To convrt or build an array to linked list
    def build(self,arr):
        self.head = Node(arr[0])
        current = self.head
        for i in arr[1:]:
            current.next = Node(i)
            current = current.next
       
    # To print the linked list
    def print_list(self):
        current = self.head
        while current:
           print(current.data, end=' -> ')
           current = current.next
        print('None')
    
    # To add a new node at the tail
    def append_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    # To add a new node at the Head
    def prepend_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    # To delete a new node at any point, Just give the key 
    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
        
    # To remove the head from the linked list
    def remove_head(self):
        if self.head is None:
            return
        self.head = self.head.next

    # To remove the tail from the linked list
    def remove_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    
    # To find the middle of a linkedList
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # To insert a new node to current Linked List middle
    def insert_into_middle(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        middle_node = self.find_middle()
        new_node.next = middle_node.next
        middle_node.next = new_node

    def reverse_linkedList(self):
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    
        
LL = linkedList()
arr = [2,4,6,8,4,3,1]
LL.build(arr)
LL.append_node(99)
LL.append_node(98)
LL.prepend_node(33)
LL.delete_node(98)
LL.remove_head()
LL.remove_tail()
LL.insert_into_middle(999)
middle = LL.find_middle()
print(middle)

LL.print_list()
