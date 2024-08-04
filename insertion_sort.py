class InsertionSort:
    def __init__(self, linked_list):
        self.linked_list = linked_list
    def sort(self):
        sorted_head = None
        current = self.linked_list.head
        while current:
            next_node = current.next
            sorted_head = self._insert_sorted(sorted_head, current)
            current = next_node
        self.linked_list.head = sorted_head
    def _insert_sorted(self, head, node):
        if head is None or node.data <= head.data:
            node.next = head
            head = node
        else:
            current = head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
        return head