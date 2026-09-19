class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        stack= []
        nums = sorted(candidates)
        def dfs(start_index, current_sum):

            if current_sum > target:
                return

            if current_sum == target:
                res.append(list(stack))
                return    

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i-1] == nums[i]:
                    continue

                stack.append(nums[i])  
                dfs(i + 1, current_sum + nums[i]) 
                stack.pop()
        dfs(0, 0)
        return res

