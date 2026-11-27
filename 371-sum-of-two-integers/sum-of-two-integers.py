class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        a = a & mask

        if a & 0x80000000:
            return ~(mask ^ a)

        return a
