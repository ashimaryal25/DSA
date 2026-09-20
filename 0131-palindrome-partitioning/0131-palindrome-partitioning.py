class Solution(object):
    def partition(self, s):
        res = []
        stack = []

        def isPalindrome(st):
            return st == st[::-1]

        def dfs(index):
            if index == len(s):
                res.append(list(stack))
                return


            for  i in range(index, len(s)):
                forwardStr = s[index : i + 1]

                if isPalindrome(forwardStr):
                    stack.append(forwardStr)
                    dfs(i + 1)
                    stack.pop()
        dfs(0)            
        return res            
                    
                    


        