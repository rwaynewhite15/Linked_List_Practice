class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def make_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def append(self, data):
        print(f"Appending value {data} to end.")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def prepend(self, data):
        print(f"Prepending value {data} to beginning.")
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        print(f"Length of Linked List: {count}")
    def delete_with_value(self, data):
        print(f"Deleting with value {data}.")
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
    def delete_at_position(self, position):
        print(f"Deleting at position {position}.")
        # Check if the linked list is empty
        if self.head is None:
            print("The list is empty.")
            return
        # Check if the position is the head
        if position == 0:
            self.head = self.head.next
            return
        # Traverse the list to find the node just before the position
        current_node = self.head
        previous_node = None
        count = 0
        while current_node and count < position:
            previous_node = current_node
            current_node = current_node.next
            count += 1
        # If the position is greater than the number of nodes
        if current_node is None:
            print("Position is out of bounds.")
            return
        # Delete the node at the position
        previous_node.next = current_node.next
        current_node = None
    def is_sorted(self):
        current = self.head
        while current and current.next:
            if current.data > current.next.data:
                print("This Linked List is Not Sorted")
                return 
            current = current.next
        print("This Linked List is Sorted")
    def display(self):
        # current_node = self.head
        # while current_node:
        #     print(current_node.data, end = " -> ")
        #     current_node = current_node.next
        #     if current_node == None:
        #         print("")
                self.size()
                self.is_sorted()
        #         return
        # print('None')
    def copy(self):
        if not self.head:
            return LinkedList()
        copied_list = LinkedList()
        current = self.head
        copied_list.head = Node(current.data)
        copied_current = copied_list.head
        while current.next:
            current = current.next
            copied_current.next = Node(current.data)
            copied_current = copied_current.next
        return copied_list