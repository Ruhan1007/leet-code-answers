class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node['#'] = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return '#' in node

            char = word[index]

            if char == '.':
                for key in node:
                    if key != '#' and dfs(node[key], index + 1):
                        return True
                return False

            if char not in node:
                return False

            return dfs(node[char], index + 1)

        return dfs(self.root, 0)