# Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/
#

from queue import Queue
class MyStack:

    def __init__(self):
        self.queue_a = Queue()
        self.queue_b = Queue()

    def move_queue(self, to_fill: Queue, to_empty: Queue) -> 'self':
        # Move all items from one queue to the other.
        while not to_empty.empty():
            to_fill.put(to_empty.get())
        return self

    def push(self, x: int) -> 'self':
        # Add element to the top of the stack.
        if self.queue_a.empty():
            self.queue_a.put(x)
            self.move_queue(self.queue_a, self.queue_b)
        else:
            self.queue_b.put(x)
            self.move_queue(self.queue_b, self.queue_a)
        return self

    def pop(self) -> int:
        # Remove the element on top of the stack and returns that element.
        if self.queue_a.empty(): return self.queue_b.get()
        return self.queue_a.get()

    def top(self) -> int:
        # Return the top element without removing it from the stack.
        top_element = self.pop()
        self.push(top_element)
        return top_element

    def empty(self) -> bool:
        # Return True if the stack is empty.
        return self.queue_a.empty() and self.queue_b.empty()
        
