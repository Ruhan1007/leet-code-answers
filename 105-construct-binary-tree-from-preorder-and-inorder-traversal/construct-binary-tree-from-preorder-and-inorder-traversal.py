
class Solution:
    def buildTree(self, preorder, inorder):
        index = {val: i for i, val in enumerate(inorder)}
        self.preIndex = 0

        def build(left, right):
            if left > right:
                return None

            # First element in preorder is the root
            root_val = preorder[self.preIndex]
            self.preIndex += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = index[root_val]

            # Build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
