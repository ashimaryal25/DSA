class Solution(object):
    def letterCombinations(self, digits):
        
        nums = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" :  "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = []
        stack = []

        def dfs(cur, cur_combo):

            if cur == len(digits):
                res.append("".join(stack))
                return

            cur_d = digits[cur]

            for c in nums[cur_d]:
                stack.append(c)

                dfs(cur + 1, cur_combo)

                stack.pop()
        dfs(0, "")
        return res



        
        