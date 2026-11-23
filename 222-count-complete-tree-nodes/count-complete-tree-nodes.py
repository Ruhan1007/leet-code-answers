class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def leftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def rightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        left = leftHeight(root)
        right = rightHeight(root)

        if left == right:
            return (1 << left) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)