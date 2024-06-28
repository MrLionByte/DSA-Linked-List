class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = newNode

    
    def printList(self):
        if self.head is None:
            print('List is empty')
            return

        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


firstNode = Node('Jhon')
secondNode = Node('Ben')
thirdNode = Node('Mathew')

linkedlist = LinkedList()
linkedlist.insert(firstNode)
linkedlist.insert(secondNode)
# linkedlist.insert(thirdNode)
linkedlist.printList()
