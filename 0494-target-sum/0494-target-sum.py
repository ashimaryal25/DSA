class Solution(object):
    def findTargetSumWays(self, nums, target):
        length = len(nums)
        memo = {}
        
        def dfs(current_index, current_sum):
            if target == current_sum and current_index >= length:
                return 1
            if current_index >= length:
                return 0  

            if (current_index, current_sum) in memo:
                return memo[(current_index, current_sum)]
                
            ans = ( 
                dfs(current_index + 1, current_sum + nums[current_index]) +
                dfs(current_index + 1, current_sum - nums[current_index])   
            )

            memo[(current_index, current_sum)] = ans
            return ans   
        
        return dfs(0, 0)
