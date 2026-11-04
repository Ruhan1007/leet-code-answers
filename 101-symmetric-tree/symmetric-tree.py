
class Solution:
    def isSymmetric(self, root):
        def isMirror(left, right):
            # Both nodes are empty
            if not left and not right:
                return True

            # Only one node is empty
            if not left or not right:
                return False

            # Check values and opposite subtrees
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))

        return isMirror(root.left, root.right)
