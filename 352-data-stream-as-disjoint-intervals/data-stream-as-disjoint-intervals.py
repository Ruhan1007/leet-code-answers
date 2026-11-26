class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        result = []

        for num in sorted(self.nums):
            if not result or num > result[-1][1] + 1:
                result.append([num, num])
            else:
                result[-1][1] = num

        return result