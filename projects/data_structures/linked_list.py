import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, value):
        # Create a new node
        newNode = Node(value)

        # Check if the linked list is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.length += 1


    def pop(self):
        # Check if the linked list is empty
        if self.head is None:
            return None
        
        # Check if there is only one node in the linked list
        temp = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        # Traverse the linked list to get the second last node
        secondLastNode = self.head
        while secondLastNode.next.next:
            secondLastNode = secondLastNode.next
        lastNode = secondLastNode.next
        secondLastNode.next = None
        self.tail = secondLastNode
        self.length -= 1
        return lastNode
        

    """
    Removes and returns the first element from the linked list.
    
    Returns:
        The node at the head of the list or None if the list is empty.
    
    Time Complexity: O(1)
    """
    def pop_first(self):
        if self.head is None:
            return None
        
        temp = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            self.head = self.head.next
            self.length -= 1
            return temp

            
    def prepend(self, value):
        # Create a new node with passed value
        newNode = Node(value)

        # Check if the linked list is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1        
        
    
    """
    Retrieve the node at the given index in the linked list.

    :param index: The index of the node to retrieve
    :return: The node at the specified index or None if the index is out of range
    """
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp
    

    """
    Insert a new node with the given value at the specified index.

    Args:
    value: The data to be inserted into the new node.
    index: The position at which to insert the new node.

    Returns:
    bool: True if insertion was successful, False if the index was out of bounds.
    """
    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False
        
        newNode = Node(value)

        if index == 0:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
            return True
        if index == self.length:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
            return True
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next

            newNode.next = temp.next
            temp.next = newNode
            self.length += 1
            return True


    """
    Set the value of the node at the specified index.

    Args:
    index (int): The index of the node whose value needs updating.
    value: The new value to set.

    Returns:
    bool: True if the value was set successfully, False otherwise.
    """
    def set(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
