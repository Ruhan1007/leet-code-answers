class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        # Calculate the length of the linked list
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Handle rotations greater than the list length
        k = k % length

        if k == 0:
            return head

        # Connect the last node to the head
        tail.next = head

        # Find the new tail
        steps = length - k
        new_tail = head

        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head