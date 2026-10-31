class Solution:
    def permute(self, nums):
        res = []
        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i+1:])
                path.pop()
        backtrack([], nums)
        return res