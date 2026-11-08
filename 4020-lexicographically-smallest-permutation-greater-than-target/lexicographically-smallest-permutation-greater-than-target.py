class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        n = len(s)
        cnt = Counter(s)
        
        def can_form(prefix):
            need = Counter(prefix)
            for c, v in need.items():
                if cnt.get(c, 0) < v:
                    return False
            return True
        
        def subtract(prefix):
            res = dict(cnt)
            for c in prefix:
                res[c] -= 1
                if res[c] == 0:
                    del res[c]
            return res
        
        for p in range(n - 1, -1, -1):
            prefix = target[:p]
            if not can_form(prefix):
                continue
            remaining = subtract(prefix)
            chosen = None
            for c in sorted(remaining):
                if c > target[p]:
                    chosen = c
                    break
            if chosen is None:
                continue
            rem2 = dict(remaining)
            rem2[chosen] -= 1
            if rem2[chosen] == 0:
                del rem2[chosen]
            suffix = "".join(c * rem2[c] for c in sorted(rem2))
            return prefix + chosen + suffix
        
        return ""