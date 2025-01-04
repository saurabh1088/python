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
    """
    A class representing a node in a singly linked list.

    Attributes:
        value: The data stored in the node.
        next (Node): Reference to the next node in the list, None if it's the last node.
    """

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    A class implementing a singly linked list data structure.

    This LinkedList uses a Node class to represent each element,
    where each node holds a value and a reference to the next node.
    The list maintains pointers to both the head (first node) and
    tail (last node) for efficient operations at both ends.

    Attributes:
        head (Node): The first node in the list.
        tail (Node): The last node in the list.
        length (int): The number of nodes in the list.

    Methods:
        __init__(value): Initializes the list with one node.
        append(value): Adds a node to the end of the list.
        pop(): Removes and returns the last node.
        pop_first(): Removes and returns the first node.
        prepend(value): Adds a node to the start of the list.
        get(index): Retrieves the node at the given index.
        insert(value, index): Inserts a new node at the specified index.
        set(value, index): Updates the value of the node at the given index.
        remove(index): Removes and returns the node at the specified index.

    Time Complexity:
        - Append/Prepend: O(1)
        - Pop/PoPFirst: O(1) for first, O(n) for last
        - Insert/Remove: O(n) in worst case due to traversal
        - Get/Set: O(n) due to traversal
    """

    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1


    def append(self, value):
        """
        Add a node with the given value to the end of the linked list.

        Args:
            value: The data to be stored in the new node.

        Returns:
            None

        Effects:
            - Increases the length of the list by 1.
            - Updates the tail of the list to the new node.
            - If the list was empty, both head and tail are set to the new node.
        """
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
        """
        Removes and returns the last node from the linked list.

        Returns:
            Node: The last node of the list or None if the list is empty.

        Effects:
            - Decreases the length of the list by 1.
            - Updates the tail of the list.
            - If the list had only one node, sets both head and tail to None.
        """
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

    
    def pop_first(self):
        """
        Removes and returns the first element from the linked list.
    
        Returns:
            The node at the head of the list or None if the list is empty.
    
        Time Complexity: O(1)
        """
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
        """
        Add a node with the given value to the beginning of the linked list.

        Args:
            value: The data to be stored in the new node.

        Returns:
            None

        Effects:
            - Increases the length of the list by 1.
            - Updates the head of the list to the new node.
            - If the list was empty, sets both head and tail to the new node.
        """
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
        
    
    def get(self, index):
        """
        Retrieve the node at the given index in the linked list.

        :param index: The index of the node to retrieve
        :return: The node at the specified index or None if the index is out of range
        """
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp
    
    
    def insert(self, value, index):
        """
        Insert a new node with the given value at the specified index.

        Args:
        value: The data to be inserted into the new node.
        index: The position at which to insert the new node.

        Returns:
        bool: True if insertion was successful, False if the index was out of bounds.
        """
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

    
    def set(self, value, index):
        """
        Set the value of the node at the specified index.

        Args:
        index (int): The index of the node whose value needs updating.
        value: The new value to set.

        Returns:
        bool: True if the value was set successfully, False otherwise.
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    
    def remove(self, index):
        """
        Remove the node at the given index from the linked list.

        Args:
        index (int): The position of the node to remove.

        Returns:
        Node: The removed node or None if the index was out of bounds.
        """
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        node_to_be_removed = temp.next
        temp.next = node_to_be_removed.next
        node_to_be_removed.next = None
        self.length -= 1
        return node_to_be_removed
    

    def reverse(self):
        if self.length < 2:
            return True

        temp = self.head
        self.head = self.tail
        self.tail = temp

        prev = None
        current = temp
        next_node = None if temp is None else temp.next

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return True

