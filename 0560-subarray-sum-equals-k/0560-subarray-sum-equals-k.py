from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = [0] * (len(nums) + 1)
        ans = 0

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        freq_map = defaultdict(int)
        freq_map[0] = 1

        for i in range(1, len(prefix_sum)):
            cur = prefix_sum[i]

            needed = cur - k

            ans += freq_map[needed]

            freq_map[cur] += 1

        return ans








        

        
        
        