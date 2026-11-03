class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        if n == 0:
            return []

        memo = {}

        def build(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]

            trees = []
            for root_val in range(start, end + 1):
                for left in build(start, root_val - 1):
                    for right in build(root_val + 1, end):
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)

            memo[(start, end)] = trees
            return trees

        return build(1, n)