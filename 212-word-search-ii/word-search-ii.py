class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['$'] = word

        m, n = len(board), len(board[0])
        result = []

        def dfs(i, j, node):
            char = board[i][j]

            if char not in node:
                return

            node = node[char]

            if '$' in node:
                result.append(node.pop('$'))

            board[i][j] = '#'

            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(x, y, node)

            board[i][j] = char

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return result