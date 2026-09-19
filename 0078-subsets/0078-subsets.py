class Solution(object):
    def subsets(self, nums):
        res = []
        stack = []

        def dfs(start_index):

            res.append(list(stack))

            for i in range(start_index, len(nums)):

                stack.append(nums[i])
                dfs(i+1)
                stack.pop()
        dfs(0)        
        return res
    