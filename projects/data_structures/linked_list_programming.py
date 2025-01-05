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

