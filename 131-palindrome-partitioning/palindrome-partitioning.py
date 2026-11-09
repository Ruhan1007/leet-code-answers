class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == n:
                result.append(path[:])
                return
            for end in range(start + 1, n + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return result