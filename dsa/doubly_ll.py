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

    def insert_at_beginning(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print()


list = DoublyLinkedList()
list.insert_at_end(10)
list.insert_at_beginning(5)
list.insert_at_end(20)
list.insert_at_end(30)
list.print_list()
