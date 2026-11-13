class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        log = n.bit_length()

        next_greater = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1]
            stack.append(i)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        up = [next_greater[:]]
        cost = [[
            nums[i] * (next_greater[i] - i)
            - (pref[next_greater[i]] - pref[i])
            for i in range(n)
        ]]

        for j in range(1, log):
            prev_up = up[-1]
            prev_cost = cost[-1]

            curr_up = [n] * n
            curr_cost = [0] * n

            for i in range(n):
                mid = prev_up[i]
                if mid < n:
                    curr_up[i] = prev_up[mid]
                    curr_cost[i] = prev_cost[i] + prev_cost[mid]
                else:
                    curr_cost[i] = prev_cost[i]

            up.append(curr_up)
            cost.append(curr_cost)

        def get_cost(l, r):
            total = 0
            cur = l

            for j in range(log - 1, -1, -1):
                nxt = up[j][cur]
                if nxt <= r:
                    total += cost[j][cur]
                    cur = nxt

            total += nums[cur] * (r - cur + 1) - (pref[r + 1] - pref[cur])
            return total

        ans = 0
        left = 0

        for right in range(n):
            while left <= right and get_cost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans