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

    def insert_at_beginning(self, value):
        temp = Node(value)
        if self.head != None:
            temp.next = self.head
            self.head = temp
        else:
            self.head = temp

    def insert_at_position(self, value, pos):
        temp = Node(value)
        if self.head != None:
            if pos == 1:
                temp.next = self.head
                self.head = temp
            else:
                t1 = self.head
                for i in range(1, pos - 1):
                    t1 = t1.next
                temp.next = t1.next
                t1.next = temp
        else:
            self.head = temp

    def delete_at_position(self, pos):
        if self.head != None:
            if pos == 1:
                self.head = self.head.next
            else:
                t1 = self.head
                for i in range(1, pos - 1):
                    t1 = t1.next
                t1.next = t1.next.next

    def print_list(self):
        t1 = self.head
        while t1 != None:
            print(t1.info, end=" ")
            t1 = t1.next


obj = SinglyLinkedList()
obj.insert_at_end(10)
obj.insert_at_end(20)
obj.insert_at_beginning(5)
obj.delete_at_position(20)
obj.print_list()
