import linked_list
import logging
import math

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# Find the middle node of the linked list. If the list has an even number of elements, return the second middle node.
def find_middle_in_linked_list(ll):
    """
    Find the middle node of a linked list.

    This function traverses the linked list once to locate the middle node. 
    If the list has an even number of nodes, it returns the node at the 
    second of the two middle positions.

    Args:
        ll (LinkedList): An instance of the LinkedList class, representing 
                         the linked list to search.

    Returns:
        Node: The middle node of the linked list, or None if the list is empty.
              - If the list has one node, that node is returned.
              - For lists with even length, the node at index length/2 is returned.

    Time Complexity:
        O(n), where n is the number of nodes in the list, since we traverse 
        the list only once.

    Space Complexity:
        O(1), as we only use a single pointer 'temp' regardless of the list size.
    """
    if ll.head is None:
        return None
    
    if ll.head.next is None:
        return ll.head
    
    temp = ll.head
    for _ in range(math.floor(ll.length / 2)):
        temp = temp.next

    return temp

# Detect if the given linked list is circular (i.e., the tail node points to a node within the list).
def is_circular_linked_list(ll):
    """
    Determine if the given linked list is circular.

    This function uses Floyd's cycle-finding algorithm (also known as the "tortoise and hare" method)
    to detect if there's a cycle in the linked list.

    Args:
        ll (LinkedList): An instance of a LinkedList class where 'head' is the first node of the list.

    Returns:
        bool:
            - True if the linked list is circular (i.e., the last node points to a node within the list).
            - False if the list is linear or empty.

    Notes:
        - Assumes 'll' has a 'head' attribute pointing to the first node of the list.
        - Each node in the list should have a 'next' attribute for this function to work correctly.
        - If the list has fewer than two nodes, it cannot be circular by definition, so it returns False.
    """
    # There is no possibility of a circular list if the list is empty or has only one node.
    if ll.head is None:
        return False

    # Initialize two pointers, slow and fast, to the first and second nodes in the list, respectively.
    slow = ll.head
    fast = ll.head.next

    while fast is not None and fast.next is not None:
        # If the slow and fast pointers meet, the list is circular.
        if slow == fast:
            return True

        # Move the slow pointer one node ahead and the fast pointer two nodes ahead.
        slow = slow.next
        fast = fast.next.next

    return False


if __name__ == "__main__":
    ll = linked_list.LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)

    middle = find_middle_in_linked_list(ll)
    logging.info(f"Middle node: {middle.value}")  # Output: Middle node: 5

    ll.append(8)
    middle = find_middle_in_linked_list(ll)
    logging.info(f"Middle node: {middle.value}")  # Output: Middle node: 6

