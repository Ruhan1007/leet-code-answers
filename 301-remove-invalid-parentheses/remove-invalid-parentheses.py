from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def isValid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                if balance < 0:
                    return False

            return balance == 0

        result = []
        visited = set()
        queue = [s]
        found = False

        while queue:
            current = queue.pop(0)

            if isValid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] not in '()':
                    continue

                if i > 0 and current[i] == current[i - 1]:
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result
