class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parse(i):
            result = set()
            current = {""}
            while i < len(expression):
                c = expression[i]
                if c == '{':
                    sub, i = parse(i + 1)
                    current = {a + b for a in current for b in sub}
                    i += 1  # Skip the closing '}'
                elif c == '}':
                    return result | current, i
                elif c == ',':
                    result |= current
                    current = {""}
                    i += 1
                else:
                    current = {a + b for a in current for b in {c}}
                    i += 1
            return result | current, i
        return sorted(parse(0)[0])