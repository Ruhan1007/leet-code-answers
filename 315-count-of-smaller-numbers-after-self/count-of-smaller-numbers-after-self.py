class Solution:
    def countSmaller(self, nums):
        arr = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(arr)}
        tree = [0] * (len(arr) + 1)

        def update(i):
            while i < len(tree):
                tree[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & -i
            return s

        ans = []
        for num in reversed(nums):
            r = rank[num]
            ans.append(query(r - 1))
            update(r)

        return ans[::-1]