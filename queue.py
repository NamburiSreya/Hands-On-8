##queue.py
QUEUE_MAX = 100

class Queue:
    def __init__(self):
        self.items = [0] * QUEUE_MAX
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % QUEUE_MAX == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % QUEUE_MAX
        self.items[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        value = self.items[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % QUEUE_MAX
        return value

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Is empty?", "Yes" if queue.is_empty() else "No")
    print("Dequeued:", queue.dequeue())
    print("Is empty?", "Yes" if queue.is_empty() else "No")


##output
Dequeued: 10
Dequeued: 20
Is empty? No
Dequeued: 30
Is empty? Yes  

# type: ignore