class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        n = len(s)
        cnt = Counter(s)
        
        odd = [c for c in cnt if cnt[c] % 2 == 1]
        if len(odd) > 1:
            return ""
        
        mid = odd[0] if odd else ""
        half_len = n // 2
        half_counts = {}
        for c in cnt:
            v = cnt[c] // 2
            if v > 0:
                half_counts[c] = v
        
        def build_pal(h):
            return h + mid + h[::-1]
        
        def can_form(prefix):
            need = Counter(prefix)
            for c, v in need.items():
                if half_counts.get(c, 0) < v:
                    return False
            return True
        
        def subtract(prefix):
            res = dict(half_counts)
            for c in prefix:
                res[c] -= 1
                if res[c] == 0:
                    del res[c]
            return res
        
        bound = target[:half_len]
        if can_form(bound):
            pal = build_pal(bound)
            if pal > target:
                return pal
        
        for p in range(half_len - 1, -1, -1):
            prefix = bound[:p]
            if not can_form(prefix):
                continue
            remaining = subtract(prefix)
            chosen = None
            for c in sorted(remaining):
                if c > bound[p]:
                    chosen = c
                    break
            if chosen is None:
                continue
            rem2 = dict(remaining)
            rem2[chosen] -= 1
            if rem2[chosen] == 0:
                del rem2[chosen]
            suffix = "".join(c * rem2[c] for c in sorted(rem2))
            h = prefix + chosen + suffix
            return build_pal(h)
        
        return ""