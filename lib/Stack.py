class Stack:

    def __init__(self, items = None, limit = 100):
        if items is None:
            self.items = []
        else:
            self.items = list(items)  # Create a new list based on the input to avoid reference issues
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            # Handle the full stack case, e.g., by raising an exception or ignoring the push
            print("Stack is full. Cannot add more items.")

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        top_of_stack = self.items[-1]
        if target in self.items:
            return top_of_stack - target
        else:
            return -1
