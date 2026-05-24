class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = temp
        temp.prev = curr

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()
