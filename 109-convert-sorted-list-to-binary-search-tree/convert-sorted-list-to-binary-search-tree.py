class Solution:
    def sortedListToBST(self, head):

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        # Find the middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect the left half
        prev.next = None

        # Create root using middle node
        root = TreeNode(slow.val)

        # Build left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
