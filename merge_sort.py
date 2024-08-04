class MergeSort:
    def __init__(self, linked_list):
        self.linked_list = linked_list
    def sort(self):
        self.linked_list.head = self._merge_sort(self.linked_list.head)
    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)
        return self._sorted_merge(left, right)
    def _get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def _sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)
        return result