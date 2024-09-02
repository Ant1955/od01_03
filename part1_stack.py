class Stack:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def push(self, item):
       self.items.append(item)

   def pop(self):
       return self.items.pop()

   def peek(self):
       return self.items[-1]
   def deep(self):
       return len(self.items)

stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())
print(stack.deep())
print(stack.peek())
