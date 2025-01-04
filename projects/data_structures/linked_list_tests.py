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

    # Test case for pop method of LinkedList class when the linked list is empty
    def test_pop_method_when_linked_list_is_empty(self):
        ll = linked_list.LinkedList(5)
        ll.head = None
        ll.tail = None
        ll.length = 0
        self.assertEqual(ll.pop(), None)

    # Test case for pop method of LinkedList class when there is only one node in the linked list
    def test_pop_method_when_linked_list_has_only_one_node(self):
        ll = linked_list.LinkedList(5)
        self.assertEqual(ll.pop().value, 5)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.length, 0)

    # Test case for pop method of LinkedList class when there are multiple nodes in the linked list
    def test_pop_method_when_linked_list_has_multiple_nodes(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.pop().value, 15)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 10)
        self.assertEqual(ll.length, 2)

    # Test case for pop_first method of LinkedList class when linked list is empty
    def test_pop_first_method_when_linked_list_is_empty(self):
        ll = linked_list.LinkedList(5)
        ll.head = None
        ll.tail = None
        ll.length = 0
        self.assertEqual(ll.pop_first(), None)

    # Test case for pop_first method of LinkedList class when there is only one node in the linked list
    def test_pop_first_method_when_linked_list_has_only_one_node(self):
        ll = linked_list.LinkedList(5)
        self.assertEqual(ll.pop_first().value, 5)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.length, 0)

    # Test case for pop_first method of LinkedList class when there are multiple nodes in the linked list
    def test_pop_first_method_when_linked_list_has_multiple_nodes(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.pop_first().value, 5)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 15)
        self.assertEqual(ll.length, 2)

    # Test case for prepend method of LinkedList class when the linked list is empty
    def test_prepend_method_when_linked_list_is_empty(self):
        ll = linked_list.LinkedList(5)
        ll.head = None
        ll.tail = None
        ll.length = 0

        # Assert list is empty
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.length, 0)

        # Prepend a new node
        ll.prepend(10)

        # Assert new node is added to the linked list
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 10)
        self.assertEqual(ll.length, 1)

    # Test case for prepend method of LinkedList class when there are multiple nodes in the linked list
    def test_prepend_method_when_linked_list_has_multiple_nodes(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        ll.prepend(0)
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 15)
        self.assertEqual(ll.length, 4)

    # Test case for get method of LinkedList class when index is out of range
    def test_get_method_when_index_is_out_of_range(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.get(4), None)

    # Test case for get method of LinkedList class when index is in range
    def test_get_method_when_index_is_in_range(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.get(1).value, 10)

    # Test case for get method of LinkedList class when index is 0
    def test_get_method_when_index_is_zero(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.get(0).value, 5)

    # Test case for insert method of LinkedList class when index is out of range
    def test_insert_method_when_index_is_out_of_range(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.insert(20, 4), False)

    # Test case for insert method of LinkedList class when list has one node and index is 0
    def test_insert_method_when_linked_list_has_one_node_and_index_is_zero(self):
        ll = linked_list.LinkedList(5)
        ll.insert(10, 0)
        self.assertEqual(ll.head.value, 10)
        self.assertEqual(ll.tail.value, 5)
        self.assertEqual(ll.length, 2)

    # Test case for insert method of LinkedList class when list has multiple nodes
    def test_insert_method_when_linked_list_has_multiple_nodes(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        ll.append(20)
        ll.insert(0, 2)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 20)
        self.assertEqual(ll.length, 5)
        self.assertEqual(ll.get(2).value, 0)

    # Test case for insert method of LinkedList class when list has multiple nodes and index is end of the list
    def test_insert_method_when_linked_list_has_multiple_nodes_and_index_is_end_of_list(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        ll.append(20)
        ll.insert(25, 4)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 25)
        self.assertEqual(ll.length, 5)
        self.assertEqual(ll.get(4).value, 25)

    # Test case for set method of LinkedList class when index is out of range
    def test_set_method_when_index_is_out_of_range(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.set(20, 4), False)

    # Test case for set method of LinkedList class when index is in range
    def test_set_method_when_index_is_in_range(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        ll.set(20, 1)
        self.assertEqual(ll.get(1).value, 20)

    # Test case for remove method of LinkedList class when index is out of range
    def test_remove_method_when_index_is_out_of_range(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.remove(4), None)

    # Test case for remove method of LinkedList class when index is in range
    def test_remove_method_when_index_is_in_range(self):
        ll = linked_list.LinkedList(5)
        ll.append(10)
        ll.append(15)
        self.assertEqual(ll.remove(1).value, 10)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 15)
        self.assertEqual(ll.length, 2)

    # Test case for remove method of LinkedList class when list is empty
    def test_remove_method_when_linked_list_is_empty(self):
        ll = linked_list.LinkedList(5)
        ll.head = None
        ll.tail = None
        ll.length = 0
        self.assertEqual(ll.remove(0), None)
        self.assertEqual(ll.remove(1), None)
        self.assertEqual(ll.remove(10), None)

if __name__ == "__main__":
    unittest.main()

