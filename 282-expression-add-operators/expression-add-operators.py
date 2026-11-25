class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(index, path, value, prev):
            if index == len(num):
                if value == target:
                    res.append(path)
                return

            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break

                s = num[index:i + 1]
                curr = int(s)

                if index == 0:
                    backtrack(i + 1, s, curr, curr)
                else:
                    backtrack(i + 1, path + '+' + s, value + curr, curr)
                    backtrack(i + 1, path + '-' + s, value - curr, -curr)
                    backtrack(i + 1, path + '*' + s,
                              value - prev + prev * curr, prev * curr)

        backtrack(0, "", 0, 0)
        return res