class Solution(object):
    def canPartition(self, nums):
        summ = 0

        length = len(nums)
        for n in nums:
            summ += n

        if summ % 2 == 1:
            return False        

        target = summ / 2

        memo = {}
        def dfs(index, current_sum):
            if current_sum == target:
                return True

            if current_sum > target:
                return False    

            if index > length - 1:
                return False  

            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            ans = (
                dfs(index+1, current_sum + nums[index]) or
                dfs(index+1, current_sum)
            )  

            memo[(index, current_sum)] = ans 

            return ans
        
        return dfs(0, 0)