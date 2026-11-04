class Solution:
    def buildTree(self, inorder, postorder):
        index = {val: i for i, val in enumerate(inorder)}
        self.postIndex = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            # Last element in postorder is the root
            root_val = postorder[self.postIndex]
            self.postIndex -= 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = index[root_val]

            # Build right subtree first
            root.right = build(mid + 1, right)

            # Build left subtree
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)
