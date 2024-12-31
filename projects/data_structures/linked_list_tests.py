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


if __name__ == "__main__":
    unittest.main()

