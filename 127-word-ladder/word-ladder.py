class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        from collections import deque
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = word[:i] + c + word[i+1:]
                    if nxt in wordSet and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))
        
        return 0