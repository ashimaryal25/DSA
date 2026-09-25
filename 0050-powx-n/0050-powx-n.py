class Solution(object):
    def myPow(self, x, n):

        def helper(c):
            if c == 0:
                return 1

            half = helper(c // 2)

            if c % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1.0 / helper(-n)

        return helper(n)