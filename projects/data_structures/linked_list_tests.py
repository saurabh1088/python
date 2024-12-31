import unittest
import linked_list

class TestLinkedList(unittest.TestCase):

    # Test cases for __init__ method of LinkedList class checks default initialization
    def test_init_linked_list_default_init(self):
        ll = linked_list.LinkedList(10)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 10)
        self.assertEqual(ll.head.next, None)
        self.assertEqual(ll.length, 1)

    # Test case for __init__ method of LinkedList class checks head and tail are pointing to same node
    def test_head_and_tail_are_poining_to_same_node(self):
        ll = linked_list.LinkedList(10)
        self.assertIs(ll.head, ll.tail)

    # Test case for append method of LinkedList class checks new node is added to linked list
    def test_append_method_adds_new_node_to_linked_list(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 10)
        self.assertEqual(ll.head.next.value, 10)
        self.assertEqual(ll.length, 2)

    # Test case for append method of LinkedList class checks new node is added to linked list when head is None
    def test_append_method_adds_new_node_to_linked_list_when_head_is_None(self):
        # Create a linked list, then set head and tail to None and length to 0
        ll = linked_list.LinkedList(5)
        ll.head = None
        ll.tail = None
        ll.length = 0

        # Assert list is empty
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.length, 0)

        # Append a new node
        ll.append(10)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 10)
        self.assertEqual(ll.length, 1)


if __name__ == "__main__":
    unittest.main()

