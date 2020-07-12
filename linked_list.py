class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return F"[data:{self.data}, next:{self.next}]"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            # adds at the end
            current.next = new_node
        else:
            # first node
            self.head = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next, self.head = self.head, new_node
        else:
            # first node
            self.head = new_node

    def insert_after_item(self, data, item):
        new_node = Node(data)
        if self.head:
            current = self.head
            while True:
                if current.data == item:
                    current.next, new_node.next = new_node, current.next
                    break
                current = current.next
                if not current:
                    break
        else:
            # first node
            self.head = new_node

    def insert_before_item(self, data, item):
        new_node = Node(data)
        previous = None
        if self.head:
            current = self.head
            while True:
                if current.data == item:
                    previous.next, new_node.next = new_node, current
                    break
                previous, current = current, current.next
                if not current:
                    break
        else:
            # first node
            self.head = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        current = self.head
        previous = None
        for i in range(position-1):
            previous, current = current, current.next
        previous.next, new_node.next = new_node, current


    def get_count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search_item(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def delete_first(self):
        self.head = self.head.next

    def delete_last(self):
        current = self.head
        while current.next:
            previous, current = current, current.next
        previous.next = None


    def delete_item(self, item):
        current = self.head
        previous = None
        while current:
            if current.data == item:
                previous.next = current.next
            previous, current = current, current.next


    def delete_by_position(self, pos):
        current = self.head
        previous = None
        for i in range(pos - 1):
            previous, current = current, current.next
        previous.next = current.next

    def reverse(self):
        head = self.head
        current = head.next
        previous = head
        head.next = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

    def get_middle_element(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer.data

    def detect_loop(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

    def remove_duplicate(self):
        current = self.head
        elements = []
        while current:
            if current.data in elements:
                previous.next = current.next
            else:
                elements.append(current.data)
                previous = current
            current = current.next


    def __str__(self):
        printable_ll = ""
        current = self.head
        while True:
            printable_ll += str(current.data) + " "
            current = current.next
            if not current:
                break
        return printable_ll
