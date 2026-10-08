class Solution(object):
    def isHappy(self, n):
        seen = set()    

        num = n
        while True:
            newnum = 0
            while num != 0:
                cur = num % 10
                newnum += cur * cur
                num = num // 10

            if newnum == 1:
                return True

            if newnum not in seen:
                seen.add(newnum)
                num = newnum
            else:
                return False   


            