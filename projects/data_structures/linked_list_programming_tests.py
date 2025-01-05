import unittest
import linked_list_programming as llp
import linked_list

class TestLinkedListProgramming(unittest.TestCase):

    # Test cases for find_middle_in_linked_list when the linked list is empty
    def test_find_middle_in_linked_list_empty(self):
        ll = linked_list.LinkedList(5)
        ll.head = None
        ll.tail = None
        ll.length = 0
        self.assertIsNone(llp.find_middle_in_linked_list(ll))


if __name__ == "__main__":
    unittest.main()


