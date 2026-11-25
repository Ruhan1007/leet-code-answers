class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1

        while queue:
            node = queue.pop(0)

            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root