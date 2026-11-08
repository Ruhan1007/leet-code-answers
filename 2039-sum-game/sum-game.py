class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sumA = sumB = 0
        qA = qB = 0
        
        for i in range(half):
            if num[i] == '?':
                qA += 1
            else:
                sumA += int(num[i])
        
        for i in range(half, n):
            if num[i] == '?':
                qB += 1
            else:
                sumB += int(num[i])
        
        diff = sumA - sumB
        qDiff = qA - qB
        
        if qDiff % 2 != 0:
            return True
        
        return diff != (-9 * qDiff) // 2