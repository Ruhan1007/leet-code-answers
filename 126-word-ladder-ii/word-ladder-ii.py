class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordSet = set(wordList)
        wordSet.add(beginWord)
        
        patterns = {}
        for w in wordSet:
            for i in range(len(w)):
                key = w[:i] + '*' + w[i+1:]
                patterns.setdefault(key, []).append(w)
        
        from collections import deque
        dist = {beginWord: 0}
        queue = deque([beginWord])
        
        while queue:
            word = queue.popleft()
            if word == endWord:
                break
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                for nxt in patterns.get(key, []):
                    if nxt not in dist:
                        dist[nxt] = dist[word] + 1
                        queue.append(nxt)
        
        if endWord not in dist:
            return []
        
        result = []
        
        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                for prev in patterns.get(key, []):
                    if prev in dist and dist[prev] == dist[word] - 1:
                        path.append(prev)
                        dfs(prev, path)
                        path.pop()
        
        dfs(endWord, [endWord])
        return result