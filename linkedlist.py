# linked_list.py
LIST_MAX = 100

class LinkedList:
    def __init__(self):
        self.data = [0] * LIST_MAX
        self.next = list(range(1, LIST_MAX)) + [-1]
        self.head = -1
        self.free_index = 0

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.free_index == -1

    def insert(self, value):
        if self.is_full():
            print("List is full")
            return
        new_node = self.free_index
        self.free_index = self.next[new_node]
        self.data[new_node] = value
        self.next[new_node] = self.head
        self.head = new_node

    def delete(self, value):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        prev = -1
        while current != -1 and self.data[current] != value:
            prev = current
            current = self.next[current]
        if current == -1:
            print("Value not found")
            return
        if prev == -1:
            self.head = self.next[current]
        else:
            self.next[prev] = self.next[current]
        self.next[current] = self.free_index
        self.free_index = current

    def display(self):
        current = self.head
        while current != -1:
            print(self.data[current], end=" ")
            current = self.next[current]
        print()

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert(30)
    linked_list.insert(20)
    linked_list.insert(10)

    print("List:", end=" ")
    linked_list.display()

    linked_list.delete(20)
    print("After deleting 20:", end=" ")
    linked_list.display()

    linked_list.insert(40)
    print("After inserting 40:", end=" ")
    linked_list.display()

    
##output
List: 10 20 30 
After deleting 20: 10 30
After inserting 40: 40 10 30