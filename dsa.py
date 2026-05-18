class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        temp = Node(value)
        if self.head != None:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def print_list(self):
        t1 = self.head
        while t1 != None:
            print(t1.info, end=" ")
            t1 = t1.next


obj = SinglyLinkedList()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_end(30)
obj.insert_at_end(40)
obj.print_list()
