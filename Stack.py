class Stack:
    # Constructor to initialize an empty list as the stack
    def __init__(self):
        self.stack = []

    # Method to add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # Method to remove and return the top item from the stack, if it's not empty
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    # Method to return the top item from the stack, if it's not empty
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Method to return the number of items in the stack
    def size(self):
        return len(self.stack)

# We can create a new stack object and use its methods to manipulate the stack:
# stack = Stack()  # Create a new stack object.
#stack.push(1)  # Add an item to the top of the stack.
#stack.push(2)  # Add another item to the top of the stack.
#stack.push(3)  # Add a third item to the top of the stack.
#print(stack.peek())  # Print the top item on the stack (3).
#stack.pop()  # Remove the top item from the stack.
#print(stack.peek())  # Print the new top item on the stack (2).
#print(stack.size())  # Print the number of items in the stack (2).