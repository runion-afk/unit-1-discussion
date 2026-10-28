"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # The newest item is placed on top, where the next pop removes it first.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            raise IndexError("cannot pop from an empty stack")
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peeking reads the most recently added value without changing the stack.
        if self.is_empty():
            raise IndexError("cannot peek at an empty stack")
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self._items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values join the back, leaving earlier arrivals at the front.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            raise IndexError("cannot dequeue from an empty queue")
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # The front is the next value that dequeue will remove.
        if self.is_empty():
            raise IndexError("cannot view the front of an empty queue")
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== STACK DEMO ===")
    browser_history = Stack()
    for page in ["Home", "Courses", "Unit 2", "Discussion"]:
        browser_history.push(page)
        print(f"Visited {page}; added it to browser history.")

    most_recent_page = browser_history.peek()
    print(f"The most recent page was {most_recent_page}.")
    print(f"Peeking left that page on top: {browser_history.peek() == most_recent_page}.")
    print("Back-button history (most recent page first):")
    while not browser_history.is_empty():
        print(f"  Returned from {browser_history.pop()}")

    for operation in ("pop", "peek"):
        try:
            if operation == "pop":
                browser_history.pop()
            else:
                browser_history.peek()
        except IndexError as error:
            print(f"An empty-stack {operation} raised IndexError: {error}.")

    one_item_stack = Stack()
    one_item_stack.push("Only item")
    print(f"Removed {one_item_stack.pop()} from a one-item stack.")
    print(f"The one-item stack was empty afterward: {one_item_stack.is_empty()}.")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    print("\n=== QUEUE DEMO ===")
    print("A print queue processes jobs in the order they were submitted (FIFO).")
    print_queue = Queue()
    for job in ["Report", "Slides", "Spreadsheet", "Photo"]:
        print_queue.enqueue(job)
        print(f"Submitted {job} to the print queue.")

    next_job = print_queue.front()
    print(f"The next job to print is {next_job}.")
    print(f"Viewing the front left that job in the queue: {print_queue.front() == next_job}.")
    print("Printing jobs in arrival order:")
    while not print_queue.is_empty():
        print(f"  Printed {print_queue.dequeue()}")

    for operation in ("dequeue", "front"):
        try:
            if operation == "dequeue":
                print_queue.dequeue()
            else:
                print_queue.front()
        except IndexError as error:
            print(f"An empty-queue {operation} raised IndexError: {error}.")

    one_item_queue = Queue()
    one_item_queue.enqueue("Single print job")
    print(f"Processed {one_item_queue.dequeue()} from a one-item queue.")
    print(f"The one-item queue was empty afterward: {one_item_queue.is_empty()}.")

if __name__ == "__main__":
    main()
