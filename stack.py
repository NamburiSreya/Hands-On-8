# stack.py
STACK_MAX = 100

class Stack:
    def __init__(self):
        self.elements = [0] * STACK_MAX
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == STACK_MAX - 1

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.elements[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        value = self.elements[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.elements[self.top]

if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element:", stack.peek())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Is empty?", "Yes" if stack.is_empty() else "No")
    print("Popped:", stack.pop())
    print("Is empty?", "Yes" if stack.is_empty() else "No")

##output
Top element: 30
Popped: 30
Popped: 20
Is empty? No
Popped: 10
Is empty? Yes
