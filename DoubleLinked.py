# Temur Khabibullaev
# 3/2/2020
import gc


class Node:
    def __init__(self, data=None):
        self.next = None
        self.prev = None
        self.data = data


class DoubleLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        last = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def del_head(self):
        if self.head == None:
            return
        else:
            if self.head != self.tail:
                self.head = self.head.next
                self.head.previous = None
            else:
                self.head = self.tail = None

    def del_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def delete_node(self, dele):
        if self.head is None or dele is None:
            return
        if self.head == dele:
            self.head = dele.next
        if dele.next is not None:
            dele.next.prev = dele.prev
        if dele.prev is not None:
            dele.prev.next = dele.next
        gc.collect()

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


ins = DoubleLinked()
