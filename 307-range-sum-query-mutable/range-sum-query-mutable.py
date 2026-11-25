class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.n = len(nums)
        self.tree = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, diff)

    def _query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)