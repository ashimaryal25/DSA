class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        stack = []

        def dfs(start_index, current_sum):
            if current_sum == target:
                res.append(list(stack))
                return

            if current_sum > target:
                return
                   
            for i in range(start_index, len(candidates)):
                stack.append(candidates[i])
                dfs(i, current_sum + candidates[i])
                stack.pop()
        dfs(0, 0)
        return res