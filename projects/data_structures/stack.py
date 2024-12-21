class Stack:

    def __init__(self):
        # Initialize the stack with empty list
        self.stack = []

    def push(self, item):
        # Append the item to the stack
        self.stack.append(item)

    def pop(self):
        # Pop the last item from the stack
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        # Return the last item from the stack
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0
    

def example_stack_data_structure():
    # Create a stack object
    stack = Stack()
    
    # Push items to the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    # Pop the last item from the stack
    print(stack.pop())  # Output: 3
    
    # Peek the last item from the stack
    print(stack.peek())  # Output: 2
    
    # Check if the stack is empty
    print(stack.is_empty())  # Output: False

