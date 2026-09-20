class Solution(object):
    def wordBreak(self, s, wordDict):
        memo = {}

        def dfs(index):
            if index == len(s):
                return True

            if index in memo:
                return memo[index]

            for i in range(index, len(s)):
                word = s[index:i + 1]

                if word in wordDict:
                    if dfs(i + 1):
                        memo[index] = True
                        return True

            memo[index] = False
            return False

        return dfs(0)