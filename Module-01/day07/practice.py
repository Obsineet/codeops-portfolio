# Day 07 Exercises — Linear Structures & Big-O

# -------------------------------
# Exercise 1: Big-O identification
# -------------------------------
# List index O(1), loop O(n), nested loop O(n^2), dict lookup O(1), binary search O(log n)

print("Exercise 1: Big-O examples")
print("List index O(1)")
print("Loop O(n)")
print("Nested loop O(n^2)")
print("Dict lookup O(1)")
print("Binary search O(log n)")
print()


# -------------------------------
# Exercise 2: Compare list vs dict lookup
# -------------------------------
accounts_list = ["ACC" + str(i) for i in range(100000)]
accounts_dict = {acc: i for i, acc in enumerate(accounts_list)}

print("Exercise 2: Lookup comparison")
print("List lookup:", "ACC99999" in accounts_list)  # O(n)
print("Dict lookup:", "ACC99999" in accounts_dict)  # O(1)
print()


# -------------------------------
# Exercise 3: Stack class
# -------------------------------
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

print("Exercise 3: Stack demo")
stack = Stack()
for x in [1, 2, 3]:
    stack.push(x)
print("Stack reversed list:", [stack.pop() for _ in range(3)])
print()


# -------------------------------
# Exercise 4: Queue with deque
# -------------------------------
from collections import deque

print("Exercise 4: Queue demo")
queue = deque()
queue.append("Alice")
queue.append("Bob")
queue.append("Charlie")
print("Serving:", queue.popleft())  # FIFO
print("Remaining queue:", list(queue))
print()


# -------------------------------
# Exercise 5: Singly linked list
# -------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

print("Exercise 5: Linked list demo")
ll = LinkedList()
ll.push_front(10)
ll.push_front(20)
ll.push_front(30)
ll.print_all()
