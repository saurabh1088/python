import unittest
import linked_list_programming as llp
import linked_list

class TestLinkedListProgramming(unittest.TestCase):

    # Test case for find_middle_in_linked_list when the linked list is empty
    def test_find_middle_in_linked_list_empty(self):
        ll = linked_list.LinkedList(5)
        ll.head = None
        ll.tail = None
        ll.length = 0
        self.assertIsNone(llp.find_middle_in_linked_list(ll))

    # Test case for find_middle_in_linked_list when the linked list has one node
    def test_find_middle_in_linked_list_one_node(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        self.assertEqual(llp.find_middle_in_linked_list(ll).value, 10)

    # Test case for find_middle_in_linked_list when the linked list has an odd number of nodes
    def test_find_middle_in_linked_list_odd(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        ll.append(20)
        ll.append(25)
        self.assertEqual(llp.find_middle_in_linked_list(ll).value, 15)

    # Test case for find_middle_in_linked_list when the linked list has an even number of nodes
    def test_find_middle_in_linked_list_even(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        ll.append(20)
        ll.append(25)
        ll.append(30)
        self.assertEqual(llp.find_middle_in_linked_list(ll).value, 20)


if __name__ == "__main__":
    unittest.main()


