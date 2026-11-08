class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ones = [i for i in range(n) if s[i] == '1']
        
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        for i in range(len(ones) - k + 1):
            length = ones[i + k - 1] - ones[i] + 1
            if length < min_len:
                min_len = length
        
        result = ""
        for start in range(n - min_len + 1):
            sub = s[start:start + min_len]
            if sub.count('1') == k:
                if result == "" or sub < result:
                    result = sub
        
        return result