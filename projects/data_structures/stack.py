class Stack:

    def __init__(self):
        # Initialize the stack with empty list
        self.stack = []

    def push(self, item):
        # Append the item to the stack
        self.stack.append(item)

    def pop(self):
        # Pop the last item from the stack
        return self.stack.pop()
    
    